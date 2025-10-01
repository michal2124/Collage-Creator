import cv2
import math
import numpy as np
import pandas as pd
from pathlib import Path, PurePath

#photos sizes
d = {'size': ['test', '9x13', '10x15', '13x18', '15x20'],
     'width': [1000, 1050, 1200, 1500, 1800],
     'height': [1000, 1500, 1800, 2100, 2400]}
df = pd.DataFrame(data=d)

def crop_image(img, y, x, h, w, scale, rot):
    ih, iw, _ = img.shape
    if y > ih or x > iw:
        raise ValueError("Cropping out of frame, change x,y parameters")
    new_img = img[y:y+h, x:x+w]
    if scale !=1: new_img = cv2.resize(new_img, (0, 0), fx=scale, fy=scale)
    if rot: new_img = cv2.rotate(new_img, cv2.ROTATE_90_CLOCKWISE)
    return new_img

def create_frame(photo):
    subset = df[df['size'] == photo]
    if subset.empty:
        raise ValueError(f"Photo '{photo}' not found in DataFrame")
    
    frame_w = subset['width'].values[0]
    frame_h = subset['height'].values[0]
    
    return np.ones((frame_h, frame_w, 3), dtype=np.uint8) * 255

def optimize(img, frame):
    ih, iw, _ = img.shape
    fh, fw, _ = frame.shape
        
    qax = math.floor(fw/iw) # arrangement a
    qay = math.floor(fh/ih)
    qa = qax*qay
    
    qbx = math.floor(fw/ih) # arrangement b - with rotation
    qby = math.floor(fh/iw)
    qb = qbx*qby
    
    if iw>ih:
        qaxr = math.floor((fw-qax*iw)/ih)
        qayr = math.floor(fh/iw)
        qa += qaxr * qayr
    else:
        qaxr = math.floor(fw/ih)
        qayr = math.floor((fh-qay*ih)/iw)
        qa += qaxr * qayr
   
    if iw>ih:
        qbxr = math.floor(fw/iw)
        qbyr = math.floor((fh-qby*iw)/ih)
        qb += qbxr * qbyr
    else:
        qbxr = math.floor((fw-qbx*ih)/iw)
        qbyr = math.floor(fh/ih)
        qb += qbxr * qbyr
    if qaxr * qayr == 0: qaxr, qayr = 0, 0
    if qbxr * qbyr == 0: qbxr, qbyr = 0, 0
    
    #print('qa', qa, 'col', qax, 'row', qay, 'col rot', qaxr, 'row rot', qayr)
    #print('qb', qb, 'col', qbx, 'row', qby, 'col rot', qbxr, 'row rot', qbyr)
    
    if qa>qb:
        return qax, qay, qaxr, qayr, 0
    elif qa<qb:
        return qbx, qby, qbxr, qbyr, 1
    else:
        if qaxr * qayr < qbxr * qbyr:
            return qax, qay, qaxr, qayr, 0
        else:
            return qbx, qby, qbxr, qbyr, 1

def paste_images(img, frame, qx, qy, qxr, qyr, rot):
    validate_arrangement(img, frame, qx, qy, qxr, qyr, rot)

    img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    h, w, _ = img.shape
    fh, fw, _ = frame.shape

    q=0
    if w>h:
        if rot: # arrangement b, rot, img w>h
            for y in range(qy): # rows
                for x in range(qx): # columns
                   y1, x1 = y*w, x*h
                   y2, x2 = y1+w, x1+h
                   frame[y1:y2, x1:x2] = img_90
                   q+=1
            e, f = 0, qy*w
            for yr in range(qyr): #rows rotated
                for xr in range(qxr): #columns rotated
                    yr1, xr1 = f+yr*h, e+xr*w
                    yr2, xr2 = yr1+h, xr1+w
                    frame[yr1:yr2, xr1:xr2] = img
                    q += 1
        else: # arrangement a, nor, img w>h
            for y in range(qy):
                for x in range(qx):
                   y1, x1 = y*h, x*w
                   y2, x2 = y1+h, x1+w
                   frame[y1:y2, x1:x2] = img
                   q+=1
            e, f = qx*w, 0
            for yr in range(qyr):
                for xr in range(qxr):
                    yr1, xr1 = f+yr*w, e+xr*h
                    yr2, xr2 = yr1+w, xr1+h
                    frame[yr1:yr2, xr1:xr2] = img_90
                    q += 1
    else:
        if rot: # arrangement b, rot, img w<h
            for y in range(qy):
                for x in range(qx):
                   y1, x1 = y*w, x*h
                   y2, x2 = y1+w, x1+h
                   frame[y1:y2, x1:x2] = img_90
                   q+=1
            e, f = qx*h, 0
            for yr in range(qyr):
                for xr in range(qxr):
                    yr1, xr1 = f+yr*h, e+xr*w
                    yr2, xr2 = yr1+h, xr1+w
                    frame[yr1:yr2, xr1:xr2] = img
                    q += 1
        else: # arrangement a, nor, img w<h
            for y in range(qy):
                for x in range(qx):
                   y1, x1 = y*h, x*w
                   y2, x2 = y1+h, x1+w
                   frame[y1:y2, x1:x2] = img
                   q+=1
            e, f = 0, qy*h
            for yr in range(qyr):
                for xr in range(qxr):
                    yr1, xr1 = f+yr*w, e+xr*h
                    yr2, xr2 = yr1+w, xr1+h
                    frame[yr1:yr2, xr1:xr2] = img_90
                    q += 1  
    #print('quantity: ', q)
    return q

def validate_arrangement(img, frame, qx, qy, qxr, qyr, rot):
    h, w, _ = img.shape
    fh, fw, _ = frame.shape
    errors = [0,0,0]
    if h > fh or w > fw:
        errors[0] = 1 #Image larger than frame
    else:
        if w>h:
            if rot:
                if qx*h > fw or qxr*w > fw:
                    errors[1] = 1 #Arrangement exceeds frame width
                if qy*w + qyr*h > fh:
                    errors[2] = 1 #Arrangement exceeds frame height
            else:
                if qx*w + qxr*h > fw:
                    errors[1] = 1
                if qy*h > fh or qyr*w > fh:
                    errors[2] = 1 
        else:
            if rot:
                if qx*h + qxr*w > fw:
                    errors[1] = 1
                if qy*w > fh or qyr*h > fh:
                    errors[2] = 1
            else:
                if qx*w > fw or qxr*h > fw:
                    errors[1] = 1
                if qy*h + qyr*w > fh:
                    errors[2] = 1
    if errors[0] == 1:
        raise ValueError("Image larger than frame")
    if errors[1] == 1 and errors[2] == 1:
        raise ValueError("Arrangement exceeds frame width and height")
    if errors[1] == 1:
        raise ValueError("Arrangement exceeds frame width")
    if errors[2] == 1:
        raise ValueError("Arrangement exceeds frame height")
        
def create_collage(collection, manual, source, photo, scale, name, show, y, x, h, w, qx, qy, qxr, qyr, rot):   
    if collection: # cut out from source picture
        img = cv2.imread(source, 1)
        img_segment = crop_image(img, y, x, h, w, scale, 0)
        name_segment = name + "_segment.jpg"
        filename_segment = PurePath(source).parent / name_segment
        cv2.imwrite(str(filename_segment), img_segment)
    else: # use source picture
        img_segment = cv2.imread(source, 1)
        img_segment = cv2.resize(img_segment, (0, 0), fx=scale, fy=scale)
    
    frame = create_frame(photo)
    
    if manual == 1: # manual rows and columns arrangement
        paste_images(img_segment, frame, qx, qy, qxr, qyr, rot)
    else: # automatic arrangement
        qx, qy, qxr, qyr, rot = optimize(img_segment, frame)
        paste_images(img_segment, frame, qx, qy, qxr, qyr, rot)
            
    name_collection = name + ".jpg"
    filename_collection = PurePath(source).parent / name_collection
    cv2.imwrite(str(filename_collection), frame)

    if show:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('Generated collage', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
    



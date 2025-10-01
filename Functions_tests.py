import cv2
import numpy as np
import pytest

from Functions import *

@pytest.fixture(params=[(5, 10), (5, 5), (10, 5)])
def sample_img(request):
    frame_h, frame_w = request.param
    img = np.arange(frame_h * frame_w * 3, dtype=np.uint8).reshape((frame_h, frame_w, 3))
    return img, frame_h, frame_w

def make_frame(h, w, color=255):
    return np.ones((h, w, 3), dtype=np.uint8) * color

# Crop tests
def test_basic_crop(sample_img):
    img, frame_h, frame_w = sample_img
    cropped = crop_image(img, y=1, x=1, h=3, w=3, scale=1, rot=False)
    assert cropped.shape == (3, 3, 3)
    assert np.array_equal(cropped[0, 0], img[1, 1])

def test_crop_with_scaling(sample_img):
    img, frame_h, frame_w = sample_img
    cropped = crop_image(img, y=0, x=0, h=2, w=2, scale=2, rot=False)
    assert cropped.shape == (4, 4, 3)

def test_crop_with_rotation(sample_img):
    img, frame_h, frame_w = sample_img
    cropped = crop_image(img, y=0, x=0, h=2, w=3, scale=1, rot=True)
    assert cropped.shape == (3, 2, 3)

def test_crop_with_scaling_and_rotation(sample_img):
    img, frame_h, frame_w = sample_img
    cropped = crop_image(img, y=0, x=0, h=2, w=3, scale=2, rot=True)
    assert cropped.shape == (6, 4, 3)

def test_out_of_bounds_crop(sample_img):
    img, frame_h, frame_w = sample_img
    cropped = crop_image(img, y=frame_h-1, x=frame_w-1, h=3, w=3, scale=1, rot=False)
    assert cropped.shape == (1, 1, 3)

def test_crop_out_of_bounds_raises(sample_img):
    img, frame_h, frame_w = sample_img
    # Pass x,y beyond image boundaries
    with pytest.raises(ValueError, match="Cropping out of frame"):
        crop_image(img, y=frame_h, x=frame_w+1, h=2, w=2, scale=1, rot=False)
    with pytest.raises(ValueError, match="Cropping out of frame"):
        crop_image(img, y=frame_h+1, x=frame_w, h=2, w=2, scale=1, rot=False)
    with pytest.raises(ValueError, match="Cropping out of frame"):
        crop_image(img, y=frame_h+1, x=frame_w+1, h=2, w=2, scale=1, rot=False)

# Frame tests        
def test_create_frame_valid():
    photo = '10x15'
    frame = create_frame(photo)
    
    expected_w = df[df['size'] == photo]['width'].values[0]
    expected_h = df[df['size'] == photo]['height'].values[0]
    
    assert frame.shape == (expected_h, expected_w, 3)
    assert np.all(frame == 255)

def test_create_frame_invalid():
    with pytest.raises(ValueError, match="Photo 'invalid' not found"):
        create_frame('invalid')
 
# Optimize tests  
def test_optimize_perfect_fit(): #all images fit perfectly to frame, no rotated images on sides
    y1, x1 = 10, 20 #images
    y2, x2 = 30, 40 #frames
    img_w = make_frame(y1, x1)
    frame_w = make_frame(y2, x2)
    img_h = make_frame(x1, y1)
    frame_h = make_frame(x2, y2)
    #qx, qy, qxr, qyr, rot = optimize(img, frame)
    assert optimize(img_w, frame_w) == (2, 3, 0, 0, 0)
    assert optimize(img_w, frame_h) == (3, 2, 0, 0, 1)
    assert optimize(img_h, frame_w) == (2, 3, 0, 0, 1)
    assert optimize(img_h, frame_h) == (3, 2, 0, 0, 0)

def test_optimize_rotated(): #images fit to frame and leave space to insert additional rotated images on sides
    y1, x1 = 20, 30 #images
    y2, x2 = 40, 110 #frames
    img_w = make_frame(y1, x1)
    frame_w = make_frame(y2, x2)
    img_h = make_frame(x1, y1)
    frame_h = make_frame(x2, y2)
    assert optimize(img_w, frame_w) == (3, 2, 1, 1, 0)
    assert optimize(img_w, frame_h) == (2, 3, 1, 1, 1)
    assert optimize(img_h, frame_w) == (3, 2, 1, 1, 1)
    assert optimize(img_h, frame_h) == (2, 3, 1, 1, 0)
 
def test_optimize_frame_smaller_than_image():
    img = make_frame(50, 50)
    frame = make_frame(30, 30)
    qx, qy, qxr, qyr, rot = optimize(img, frame)
    assert (qx, qy, qxr, qyr) == (0, 0, 0, 0)

# Paste tests
def test_paste_quantity():
    y1, x1 = 20, 30 #images
    y2, x2 = 40, 110 #frames
    img_w = make_frame(y1, x1, 100)
    frame_w = make_frame(y2, x2, 255)
    img_h = make_frame(x1, y1, 100)
    frame_h = make_frame(x2, y2, 255)
    assert paste_images(img_w, frame_w, 3, 2, 1, 1, 0) == 7
    assert paste_images(img_w, frame_h, 2, 3, 1, 1, 1) == 7
    assert paste_images(img_h, frame_w, 3, 2, 1, 1, 1) == 7
    assert paste_images(img_h, frame_h, 2, 3, 1, 1, 0) == 7

def test_paste_location():
    y1, x1 = 20, 30 #images
    y2, x2 = 40, 110 #frames
    img_w = make_frame(y1, x1, 100)
    frame_w = make_frame(y2, x2, 255)
    frame_wr = make_frame(y2, x2, 255)
    img_h = make_frame(x1, y1, 100)
    frame_h = make_frame(x2, y2, 255)
    frame_hr = make_frame(x2, y2, 255)
    
    paste_images(img_w, frame_w, 1, 1, 0, 0, 0) # arrangement a, nor, img w>h, frame w>h
    assert np.all(frame_w[0:y1, 0:x1] == 100)
    paste_images(img_h, frame_h, 1, 1, 0, 0, 0) # arrangement a, nor, img w<h, frame w<h
    assert np.all(frame_h[0:x1, 0:y1] == 100)  
    paste_images(img_h, frame_wr, 1, 1, 0, 0, 1) # arrangement b, rot, img w<h, frame w>h
    assert np.all(frame_wr[0:y1, 0:x1] == 100)   
    paste_images(img_w, frame_hr, 1, 1, 0, 0, 1) # arrangement b, rot, img w>h, frame w<h
    assert np.all(frame_hr[0:x1, 0:y1] == 100)
    
def test_paste_img_larger_than_frame():
    img = make_frame(50, 50)
    frame = make_frame(30, 30)
    with pytest.raises(ValueError, match="Image larger than frame"):
        paste_images(img, frame, 1, 1, 0, 0, 0)
        
def test_paste_exceeding_arrangement():
    y, x = 10, 20
    img_w = make_frame(y, x, 100)
    img_h = make_frame(x, y, 100)
    frame = make_frame(40, 60, 255)
    
    # arrangement a, nor, img w>h - max quantities: qx=2, qy=4, qxy=2, qyr=2
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_w, frame, 3, 4, 2, 2, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_w, frame, 2, 4, 3, 2, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_w, frame, 2, 5, 2, 2, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_w, frame, 2, 4, 2, 3, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width and height"):
        paste_images(img_w, frame, 3, 5, 3, 3, 0)

    # arrangement b, rot, img w>h - max quantities: qx=6, qy=1, qxy=3, qyr=2
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_w, frame, 7, 1, 3, 3, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_w, frame, 6, 1, 4, 2, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_w, frame, 6, 2, 3, 2, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_w, frame, 6, 1, 3, 3, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width and height"):
        paste_images(img_w, frame, 7, 2, 4, 3, 1)

    # arrangement a, nor, img w<h - max quantities: qx=6, qy=1, qxy=3, qyr=2
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_h, frame, 7, 1, 3, 3, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_h, frame, 6, 1, 4, 2, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_h, frame, 6, 2, 3, 2, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_h, frame, 6, 1, 3, 3, 0)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width and height"):
        paste_images(img_h, frame, 7, 2, 4, 3, 0)

    # arrangement b, rot, img w<h - max quantities: qx=2, qy=4, qxy=2, qyr=2
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_h, frame, 3, 4, 2, 2, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width"):
        paste_images(img_h, frame, 2, 4, 3, 2, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_h, frame, 2, 5, 2, 2, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame height"):
        paste_images(img_h, frame, 2, 4, 2, 3, 1)
    with pytest.raises(ValueError, match="Arrangement exceeds frame width and height"):
        paste_images(img_h, frame, 3, 5, 3, 3, 1)
    
# Collection tests
def test_create_collage_no_file_error(tmp_path):
    source_path = tmp_path / "source.jpg"
    dummy_img = np.ones((20, 20, 3), dtype=np.uint8) * 255
    cv2.imwrite(str(source_path), dummy_img)
    
    try:
        create_collage(collection=False, manual=0, source=str(source_path), photo='test', scale=1, name='dummy', show=False,
                       y=0, x=0, h=10, w=10, qx=1, qy=1, qxr=0, qyr=0, rot=0)
    except FileNotFoundError:
        pytest.fail("create_collage raised FileNotFoundError unexpectedly")  

    

import cv2
import numpy as np
import tensorflow as tf
import os

# Load the saved model
model = tf.keras.models.load_model('model02_cnn.h5')

# Labels for all the alphabets (lowercase letters)
labels = [chr(i) for i in range(97, 123)]  # ['a', 'b', 'c', ..., 'z']

# Path to the folder containing images
image_folder = 'D:/Projects/ML-Hackathon/ppt'
image_files = os.listdir(image_folder)
current_image_index = 0
current_image = None

# Function to load a new image
def load_image(index):
    global current_image
    image_path = os.path.join(image_folder, image_files[index])
    current_image = cv2.imread(image_path)
    if current_image is not None:
        current_image = cv2.resize(current_image, (500, 500))  # Resize for display
    return current_image

# Load the first image
load_image(current_image_index)

# Initialize a canvas for drawing
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

while True:
    if current_image is not None:
        # Show the current image and canvas
        combined_image = np.vstack((current_image, canvas))
        cv2.imshow('Paint Application', combined_image)

    key = cv2.waitKey(10) & 0xFF

    if key == ord('a'):  # If 'a' is pressed
        print("Drawing mode activated")
        # Draw on the canvas (add a white rectangle for now)
        cv2.rectangle(canvas, (100, 100), (400, 400), (255, 255, 255), -1)  # White rectangle

    elif key == ord('y'):  # If 'y' is pressed
        print("Clearing drawing")
        # Clear the canvas
        canvas.fill(0)

    elif key == ord('q'):  # If 'q' is pressed
        break

    elif key == 82:  # Right arrow key: Load next image
        current_image_index = (current_image_index + 1) % len(image_files)
        load_image(current_image_index)

    elif key == 84:  # Left arrow key: Load previous image
        current_image_index = (current_image_index - 1) % len(image_files)
        load_image(current_image_index)

    # If the image is not None, update the canvas
    if current_image is not None:
        cv2.imshow('Paint Application', np.vstack((current_image, canvas)))

# Release resources
cv2.destroyAllWindows()

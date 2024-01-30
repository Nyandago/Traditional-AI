import cv2

# Function to detect faces and draw boxes around them
def detect_faces_and_draw_boxes(image_path):
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the image with boxes
    output_path = image_path.replace('.jpg', '_faces.jpg')
    cv2.imwrite(output_path, img)

    return output_path

# Example usage
image_path = 'no-face.png'
output_path = detect_faces_and_draw_boxes(image_path)
print(output_path)
print(f"Saved boxed image at: {output_path}")

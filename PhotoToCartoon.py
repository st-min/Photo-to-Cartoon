import cv2 as cv

def photo_to_cartoon(image_path, output_path):
    # Read the image
    image = cv.imread(image_path)

    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Apply a median blur to reduce noise
    blurred = cv.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

    # Apply a bilateral filter to smooth the image
    color = cv.bilateralFilter(image, 9, 250, 250)
    cv.imshow("color", color)
    cv.waitKey(0)

    # Combine the edges and color image
    cartoon = cv.bitwise_and(color, color, mask=edges)

    # Save the cartoon image
    cv.imwrite(output_image, cartoon)

    # Display the cartoon image
    cv.imshow("Cartoon", cartoon)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Example usage
input_image = "/PATH/TO/IMAGE.jpg"
output_image = "/PATH/TO/OUTPUT.jpg"
photo_to_cartoon(input_image, output_image)

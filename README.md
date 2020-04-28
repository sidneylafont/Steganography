# Steganography

A basic Steganographer, meaning it hides messages (up to 1000000 characters) in images

to encode a message using terminal:

        $ cd Steganography
        $ python encoder.py path-to-image "hidden message"

This will add the image post.png, which contains the message to the images folder 

to decode a message using terminal:

        $ cd Steganography
        $ python decoder.py path-to-image 
        
This will print the hidden message

# Example

For example to hide the message "Steganography is cool" in pre1.jpg:

        $ cd Steganography
        $ python encoder.py images/pre1.jpg "Steganography is cool"
        
Then to decode that message:

        $ cd Steganography
        $ python decoder.py images/post.png

# Packages

- Pillow (PIL)
- numpy
- sys
- string


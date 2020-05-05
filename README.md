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

For example to hide the message "Steganography is really really cool" in pre1.jpg:

        $ cd Steganography
        $ python encoder.py images/pre1.jpg "Steganography is really really cool"
        
Then to decode that message:

        $ cd Steganography
        $ python decoder.py images/post.png
        
Below are the images pre and post encoding (they look like the exact same picture):

![pre1.jpg](/images/pre1.jpg)
![post.png](/images/post.png)

# Packages

- Pillow (PIL)
- numpy
- sys
- string


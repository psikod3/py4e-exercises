""" 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line
below. Convert the extracted value to a floating point number and print it out. """

# py ch06e05_strings.py

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
sliced = text[pos:]
print(float(sliced))

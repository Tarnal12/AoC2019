import itertools

with open('Day08Input.txt', 'r') as f:
    width = 25
    height = 6
    layer_size = width * height

    least_zeroes = width * height
    most_colored_layer = -1

    # Blank image
    image = {}
    for i in range(150):
        image[i] = '2'

    for layer in iter(lambda: f.read(layer_size), ''):
        if layer == '':
            break

        for pixel in range(len(layer)):
            if image[pixel] == '2':
                image[pixel] = layer[pixel]

        num_zeroes = layer.count('0')
        if num_zeroes < least_zeroes:
            least_zeroes = num_zeroes
            most_colored_layer = layer

    print("CHECKSUM = %d" % most_colored_layer.count('1') * most_colored_layer.count('2'))
    #print(image)

    printed_str = ''
    index = 0
    for i in range(height):
        for j in range(width):
            if image[index] == '1':
                printed_str = printed_str + '#'
            else:
                printed_str = printed_str + ' '
            index = index + 1
        printed_str = printed_str + '\n'
    print(printed_str)

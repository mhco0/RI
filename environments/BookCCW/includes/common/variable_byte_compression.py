
class VariableByteCompression:

    @staticmethod
    def encode(integer):
        
        byte_array = integer.to_bytes(4, 'little')
        compress_byte_array = bytearray()
        byte_view = 0 

        #print("byte array: ")
        #print(format(int.from_bytes(byte_array, 'little'), "#032b"))
        #print()
        # encode
        byte_view = byte_array[0]
        byte_view |= 0x80 
        compress_byte_array += byte_view.to_bytes(1, 'little')

        #print("first byte with 1 setted: ")
        #print(format(byte_view, "#032b"))
        #print()

        byte_view = (byte_array[0] >> 7)

        #print("first byte after first shift: ")
        #print(format(byte_view, "#032b"))
        #print()

        for i in range(1, len(byte_array)):
            #print("byte_array[" + str(i) + "] with right shitf: ")
            #print(format(byte_array[i] << (i), "#032b"))
            #print()
            byte_view |= (byte_array[i] << (i))
            #print("byte_view with top 7 bits added:")
            #print(format(byte_view, "#032b")) 
            #print()
            byte_view &= ~(1 << 7)
            byte_view &= 255
            #print("byte_view after removing last bit: ")
            #print(format(byte_view, "#032b"))
            compress_byte_array += byte_view.to_bytes(1, 'little')
            byte_view = (byte_array[i] >> (7 - i))
            
        if byte_view:
            compress_byte_array += byte_view.to_bytes(1, 'little')
            #print("still some data left (all data):")
            #print(format(int.from_bytes(compress_byte_array, 'little'), "#032b"))
            #print()
            return compress_byte_array

        # clean
        need_to_pop = 0

        for byte in compress_byte_array[::-1]:
            if not byte:
                need_to_pop += 1
            else:
                break

        while need_to_pop:
            compress_byte_array.pop()
            need_to_pop -= 1

        #print("how become :")
        #print(format(int.from_bytes(compress_byte_array, 'little'), "#032b"))
        #print()

        return compress_byte_array
            

    @staticmethod
    def decode(byte_array):
        value = 0

        for i in range(len(byte_array)):
            byte = byte_array[i]
            byte &= ~(1 << 7)
            value |= (byte << (7 * i))
            
        return value    
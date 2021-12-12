
class VariableByteCompression:

    @staticmethod
    def encode(integer):  
        byte_array = integer.to_bytes(4, 'little')
        compress_byte_array = bytearray()
        byte_view = 0 

        # encode
        byte_view = byte_array[0]
        byte_view |= 0x80 
        compress_byte_array += byte_view.to_bytes(1, 'little')

        byte_view = (byte_array[0] >> 7)

        for i in range(1, len(byte_array)):
            byte_view |= (byte_array[i] << (i))
            byte_view &= ~(1 << 7)
            byte_view &= 255
            compress_byte_array += byte_view.to_bytes(1, 'little')
            byte_view = (byte_array[i] >> (7 - i))
            
        if byte_view:
            compress_byte_array += byte_view.to_bytes(1, 'little')
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

        return compress_byte_array
            

    @staticmethod
    def decode(byte_array):
        value = 0

        for i in range(len(byte_array)):
            byte = byte_array[i]
            byte &= ~(1 << 7)
            value |= (byte << (7 * i))
            
        return value    
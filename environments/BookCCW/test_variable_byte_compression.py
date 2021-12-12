from includes.common.variable_byte_compression import VariableByteCompression

def smoke_test():
    assert(int.from_bytes(VariableByteCompression.encode(5), 'little') == 133)
    assert(int.from_bytes(VariableByteCompression.encode(824), 'little') == 1720)
    assert(int.from_bytes(VariableByteCompression.encode(214577), 'little') == 855217)
    assert(VariableByteCompression.decode(VariableByteCompression.encode(5)) == 5)
    assert(VariableByteCompression.decode(VariableByteCompression.encode(824)) == 824)
    assert(VariableByteCompression.decode(VariableByteCompression.encode(214577)) == 214577)

def complex_test():
    for i in range(1 << 32):
        assert(VariableByteCompression.decode(VariableByteCompression.encode(i)) == i)
        print(i, end='\r')

    #for i in range(4):
        #assert(VariableByteCompression.decode(VariableByteCompression.encode(1 << (8 * i))) == (1 << (8 * i)))

if __name__ == "__main__":
    smoke_test()
    complex_test()
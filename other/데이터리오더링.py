if __name__ == "__main__":
    prev = input()
    prev = "0x" + prev

    prev = int(prev,0)

    post = 0
    val = prev >> 26 & 0x3F
    post |= val << 18

    val = prev >> 23 & 0x7
    post |= val << 13

    val = prev >> 19 & 0xF
    post |= val << 0

    val = prev >> 15 & 0xF
    post |= val << 24

    val = prev >> 11 & 0xF
    post |= val << 4

    val = prev >> 9 & 0x3
    post |= val << 16

    val = prev >> 4 & 0x1F
    post |= val << 8

    val = prev & 0xF
    post |= val << 28

    result = str(hex(post))[2:]
    print(result)
    # 491A8AC4

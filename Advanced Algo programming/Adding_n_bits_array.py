
A = [1,0,1,0,1]
B = [0,1,0,1,0]

def binaryAddition(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0

    for i in range(n):
        # Add the corresponding bits from A and B, along with the carry
        temp_sum = A[i] + B[i] + carry

        # Determine the current bit in the result C and update carry
        C[i] = temp_sum % 2
        carry = temp_sum // 2

    # Handle the last bit and any remaining carry
    C[n] = carry

    return C

binaryAdditio

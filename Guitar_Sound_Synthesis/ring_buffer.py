import stdarray
import stdio
import sys


# Create and return a ring buffer, with the given maximum capacity and with all
# elements initialized to None. A ring buffer is represented as a list
# of four elements: the buffer (buff) itself as a list; number of elements
# (size) currently in buff; the index (first) of the least recently
# inserted item; and the index (last) one beyond the most recently
# inserted item.
def create(capacity):
    buff = stdarray.create1D(capacity, None)
    rb = stdarray.create1D(4, 0)
    rb[0] = buff
    return rb


# Return the number of items currently in the buffer rb.
def size(rb):
    return rb[1]


# Return True if the buffer rb is empty and False otherwise.
def is_empty(rb):
    return rb[1] == 0


# Return True if the buffer rb is full and False otherwise.
def is_full(rb):
    return rb[1] == len(rb[0])


# Add item x to the end of the buffer rb.
def enqueue(rb, x):
    if is_full(rb):
        sys.exit('Error: cannot enqueue a full buffer')
    else:
        rb[0][rb[3]] = x
        rb[1] = (rb[1]+1)
        rb[3] = (rb[3]+1) % len(rb[0])


# Delete and return item from the front of the buffer rb.
def dequeue(rb):
    if is_empty(rb):
        sys.exit('Error: cannot dequeue an empty buffer')
    else:
        temp = rb[0][rb[2]]
        rb[1] = (rb[1]-1)
        rb[2] = (rb[2]+1) % len(rb[0])
        return temp


# Return (but do not delete) item from the front of the buffer rb.
def peek(rb):
    if is_empty(rb):
        sys.exit('Error: cannot peek an empty buffer')
    return rb[0][rb[2]]


# Test client [DO NOT EDIT].
def main():
    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    main()

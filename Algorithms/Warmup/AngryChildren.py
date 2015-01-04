def find_minimum_unfairness(packets, num_children):
    """
    Determine the lowest "unfairness" for distributing the given packets. This means the lowest difference between the
    maximum value of a subset of size num_children of the packets and the minimum value of the same subset is minimized
    :param packets: an array of integers which correspond to the size of the packets
    :param num_children: the number of children to distribute the packets to
    :return: the minimum "unfairness" value attainable
    """

    # Sort by size
    sorted_packets = sorted(packets)

    min_unfairness = sorted_packets[num_children - 1] - sorted_packets[0]
    for idx in range(len(sorted_packets) - num_children + 1):
        unfairness = sorted_packets[idx + num_children - 1] - sorted_packets[idx]
        if unfairness < min_unfairness:
            min_unfairness = unfairness

    return min_unfairness


def run():
    """
    "Main" method. Usage is:
        User inputs the number of packets, N
        User inputs the number of children, K
        User inputs the size of each of the N packets

        Program prints the minimum possible unfairness
    :return: None, prints to stdout
    """

    num_packets = int(input())
    num_children = int(input())

    packets = []
    for dummy in range(num_packets):
        packets.append(int(input()))

    print(find_minimum_unfairness(packets, num_children))


run()
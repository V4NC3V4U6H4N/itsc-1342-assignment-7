# Vance Vaughan - Assignment 7

def dissect_packet(src_ip, dst_ip, protocol, payload_bytes, flags=None):
    packet = {
        "src": src_ip,
        "dst": dst_ip,
        "proto": protocol.upper(),
        "length": payload_bytes if payload_bytes > 0 else 0,
        # I know this is horrible to read, but
        # I thought it was funny to do it this way
        "syn_flag": not(not flags or not "SYN" in flags)
    }
    
    # if flags and "SYN" in flags:
    #     packet["syn_flag"] = True

    return packet 
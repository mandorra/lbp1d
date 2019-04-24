def LBP1D(signal,p):

    # Signal is a 1D numpy array and
    # p is the size of the neighborhood

    import numpy as np

    if p % 2 != 0 :
        print("Neighbourhood p value must be even!!")
        raise

    lbp = np.zeros(len(signal)-p,dtype=int)

    for i in range(p // 2,len(signal) - (p // 2)):

        # Reference samples
        center = signal[i]
        start1 = i - (p // 2)
        end1 = i
        start2 = i + 1
        end2 = i  + (p // 2) + 1
        ran = np.r_[start1:end1,start2:end2]

        # Get neighborhood
        neir = signal[ran]
        neir = np.sign(neir - center)
        neir[neir == -1] = 0

        # Binary to decimal
        lbp[i - (p//2)] = int(str(neir.tolist())[1:-1].replace(',', '').replace(' ', '').replace('.',''), 2)

    return lbp

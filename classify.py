def butter_lowpass(cutoff, fs, order=5):
    from scipy import signal
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, fs, cutoff, order=5):
    from scipy import signal
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def classify(sig):   
    from scipy import signal
    sig = sig.copy()/max(sig)
    
    prom = 0.004
    
    if min(sig) < -0.3:
        return '3'
    
    # Identify obvious peaks above a threshold
    peaks, _ = signal.find_peaks(sig, prominence=prom)
    peaks = [y for y in peaks if sig[y] >= 0.35]
    
    # If the are many or no obvious peaks, reject
    if len(peaks) >= 3 or len(peaks) == 0:
        return '3'
    
    if len(peaks) == 2:
        
        # If the 2 peaks are too far, abnormal
        if peaks[1] - peaks[0] > 65:
            return '3'
        
        # If the first peak is significantly larger than the second
        if (sig[peaks[0]] - sig[peaks[1]]) > 0.1:
            # Abnormal peak placement
            if peaks[1] - peaks[0] < 20 or peaks[0] > 25:
                return '3'
            
            # Dicrotic notch detection
            # If there is a peak in the inverted signal between the 2 detected peaks
            # And it is not too far down or up
            p2, _ = signal.find_peaks(-sig)
            notch_peaks = [p for p in p2 \
                           if p < peaks[1] \
                           and p > peaks[0] \
                           and sig[p] < sig[peaks[1]]]
            

            # Exclude the edges, because they are typically not important and may have small bumps
            ps, _ = signal.find_peaks(sig[10:85])
            ps += 10
            nps, _ = signal.find_peaks(-sig[10:85])
            nps += 10
            if len(notch_peaks) == 1: # 2 Clear peaks + notch

                # Check if signal is too unreliable (Many peaks)
                # or peaks within the sensitive area between 
                # systolic and diastolic peak
                if len(ps) >= 3 \
                    or len(nps) >= 2 \
                    or len([p for p in ps if p < peaks[1] + 15 and p > peaks[0] - 10]) > 2 \
                    or len([np for np in nps if np < peaks[1] + 15 and np > peaks[1] - 10]) > 1:
                    
                    return '3'
                
                # If the dicrotic notch is extremely low
                d_notch = notch_peaks[0]
                if sig[d_notch] > sig[peaks[1]] - 40:
                    return '2L'
                else:
                    return '3'
            else:
                # If the signal is too unstable
                if len(ps) >= 3:
                    return '3'
                return '1L' # No clear notch

        # If the peaks are nearly equal
        else:
            ps, _ = signal.find_peaks(sig[:80])
            nps, _ = signal.find_peaks(-sig[:80])
            
            # Identify the notch between the two peaks
            notch_peaks = [p for p in nps \
               if p < peaks[1] \
               and p > peaks[0] \
               and sig[p] < sig[peaks[1]]]

            # If there are many peaks, more than 1 notch, or the notch is lower than normal, reject    
            if len(ps) >= 3 \
                or len(nps) >= 2 \
                or len(notch_peaks) > 1 \
                or len(notch_peaks) < 1 \
                or sig[notch_peaks[0]] < min(sig[peaks[0]], sig[peaks[1]]) - 0.15:
                return '3'
            return '2E'
            
    else:        
        # If the peak is far to the left
        if peaks[0] <= 25:
            ps, _ = signal.find_peaks(sig)
            nps, _ = signal.find_peaks(-sig)
            if len(ps) > 2 or len(nps) >= 2: # If there are too many peaks in the wave, reject
                    return '3'
            return '1L'
        
        return '1'
    

def classify_smooth(sig):   
    from scipy import signal
    sig = butter_lowpass_filter(sig.copy()/max(sig), 100, 10)
    
    prom = 0.004
    
    if min(sig) < -0.3:
        return '3'
    
    # Identify obvious peaks above a threshold
    peaks, _ = signal.find_peaks(sig, prominence=prom)
    peaks = [y for y in peaks if sig[y] >= 0.35]
    
    # If the are many or no obvious peaks, reject
    if len(peaks) >= 3 or len(peaks) == 0:
        return '3'
    
    if len(peaks) == 2:
        
        # If the 2 peaks are too far, abnormal
        if peaks[1] - peaks[0] > 65:
            return '3'
        
        # If the first peak is significantly larger than the second
        if (sig[peaks[0]] - sig[peaks[1]]) > 0.1:
            # Abnormal peak placement
            if peaks[1] - peaks[0] < 20 or peaks[0] > 25:
                return '3'
            
            # Dicrotic notch detection
            # If there is a peak in the inverted signal between the 2 detected peaks
            # And it is not too far down or up
            p2, _ = signal.find_peaks(-sig)
            notch_peaks = [p for p in p2 \
                           if p < peaks[1] \
                           and p > peaks[0] \
                           and sig[p] < sig[peaks[1]]]
            

            # Exclude the edges, because they are typically not important and may have small bumps
            ps, _ = signal.find_peaks(sig[10:85])
            ps += 10
            nps, _ = signal.find_peaks(-sig[10:85])
            nps += 10
            if len(notch_peaks) == 1: # 2 Clear peaks + notch

                # Check if signal is too unreliable (Many peaks)
                # or peaks within the sensitive area between 
                # systolic and diastolic peak
                if len(ps) >= 3 \
                    or len(nps) >= 2 \
                    or len([p for p in ps if p < peaks[1] + 15 and p > peaks[0] - 10]) > 2 \
                    or len([np for np in nps if np < peaks[1] + 15 and np > peaks[1] - 10]) > 1:
                    
                    return '3'
                
                # If the dicrotic notch is extremely low
                d_notch = notch_peaks[0]
                if sig[d_notch] > sig[peaks[1]] - 40:
                    return '2L'
                else:
                    return '3'
            else:
                # If the signal is too unstable
                if len(ps) >= 3:
                    return '3'
                return '1L' # No clear notch

        # If the peaks are nearly equal
        else:
            ps, _ = signal.find_peaks(sig[:80])
            nps, _ = signal.find_peaks(-sig[:80])
            
            # Identify the notch between the two peaks
            notch_peaks = [p for p in nps \
               if p < peaks[1] \
               and p > peaks[0] \
               and sig[p] < sig[peaks[1]]]

            # If there are many peaks, more than 1 notch, or the notch is lower than normal, reject    
            if len(ps) >= 3 \
                or len(nps) >= 2 \
                or len(notch_peaks) > 1 \
                or len(notch_peaks) < 1 \
                or sig[notch_peaks[0]] < min(sig[peaks[0]], sig[peaks[1]]) - 0.15:
                return '3'
            return '2E'
            
    else:
        # At this point, there should only be 1 peak in the whole wave
#         peaks, _ = signal.find_peaks(sig, prominence=0.01)
#         if len(peaks) > 1:
#             return '3h'
        
        # If the peak is far to the left
        if peaks[0] <= 25:
            ps, _ = signal.find_peaks(sig)
            nps, _ = signal.find_peaks(-sig)
            if len(ps) > 2 or len(nps) >= 2: # If there are too many peaks in the wave, reject
                    return '3'
            return '1L'
        
        return '1'
    
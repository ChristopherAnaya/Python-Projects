def good_vs_evil(good, evil):
        gl = good.split()
        el = evil.split()
        gv = [1, 2, 3, 3, 4, 10]
        ev = [1, 2, 2, 2, 3, 5, 10]
        for x in el:
            if x == " ":
                el.remove(x)
        for x in gl:
            if x == " ":
                gl.remove(x)
        for x in range(0, len(gv)):
            gl[x] = gv[x] * int(gl[x])
        for x in range(0, len(ev)):
            el[x] = ev[x] * int(el[x])
        gs = sum(gl)
        es = sum(el)
        if gs > es:
            return "Battle Result: Good triumphs over Evil"
        elif gs < es:
            return "Battle Result: Evil eradicates all trace of Good"
        else:
            return "Battle Result: No victor on this battle field"

print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))




    

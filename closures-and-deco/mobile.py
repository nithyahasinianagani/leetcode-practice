numbers = sorted([p[-10:] for p in l])
        formatted = ["+91 " + p[:5] + " " + p[5:] for p in numbers]
        return f(formatted)
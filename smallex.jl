using PyCall

function score(a,b,c,d)
    print("score called", a, b, c, d)
    return 1.0
end

pushfirst!(PyVector(pyimport("sys")."path"), "")
b = pyimport("smallex")
pyimport("importlib").reload(b)

b.call_from_julia(score)




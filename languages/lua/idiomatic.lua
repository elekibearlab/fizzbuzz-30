local rules = {
    {3, "Fizz"},
    {5, "Buzz"},
}

local function fizzbuzz(n)
    local parts = {}
    for _, rule in ipairs(rules) do
        if n % rule[1] == 0 then
            parts[#parts + 1] = rule[2]
        end
    end
    return #parts > 0 and table.concat(parts)
        or tostring(n)
end

for n = 1, 100 do
    print(fizzbuzz(n))
end

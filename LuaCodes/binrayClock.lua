-- Decimal to BinaryConverter

local array = require("array")

function BinaryConverter(num)
	local bin = {}

	while num > 0 do
		table.insert(bin, math.fmod(num, 2))
		num = math.floor(num / 2)
	end

	bin = array.reverse(bin)
	return bin
end

local time = { 0, 10, 12, 0 }

--Clock
local binaryClock = {}
for i = 1, 5 do
	binaryClock[i] = {} -- create a new row
	for j = 1, 8 do
		binaryClock[i][j] = 0
	end
end

print(table.concat(BinaryConverter(10), ""))

for _, line in ipairs(binaryClock) do
	print(table.concat(line))
end

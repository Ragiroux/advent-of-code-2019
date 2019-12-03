defmodule Advent2Part2Test do
  require Timeframe
  use ExUnit.Case
  doctest Advent2Part2


  test "part2" do
    result = Advent2Part2.part2()
    IO.inspect result
    end

end

defmodule Advent2Test do
  use ExUnit.Case
  doctest Advent2

  test "part1" do
    result = Advent2.part1()
    IO.inspect result
    assert result == [30,1,1,4,2,5,6,0,99]
  end
end

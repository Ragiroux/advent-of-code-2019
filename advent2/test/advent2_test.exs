defmodule Advent2Test do
  use ExUnit.Case
  doctest Advent2

  test "part1" do
    result = Advent2.part1()
    IO.inspect result
    assert result |> Enum.at(0) == 2894520
  end
end

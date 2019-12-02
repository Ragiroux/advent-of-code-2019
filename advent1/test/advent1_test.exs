defmodule Advent1Test do
  use ExUnit.Case
  doctest Advent1

  test "read file" do
    Advent1.readFile()
  end

  test "fuel for santa" do
    result = Advent1.part2()
    assert 4925580.0 == result
  end

end

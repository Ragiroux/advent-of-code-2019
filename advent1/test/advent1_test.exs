defmodule Advent1Test do
  require Timeframe

  use ExUnit.Case
  doctest Advent1

  test "read file" do
    Advent1.readFile()
  end

  Timeframe.execute "part2" do
    result = Advent1.part2()
    assert 4925580.0 == result
  end

end

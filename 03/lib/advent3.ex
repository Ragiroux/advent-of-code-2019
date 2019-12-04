defmodule Advent3 do

  def part1 do
    cable1 = readFile("input1.txt")
    cable2 = readFile("input2.txt")

    cable1 |> IO.puts
    cable2 |> IO.puts
  end

  def moveCable(cable, coord) do
    
  end

  def readFile(filename) do
    File.read!(filename)
  end

end

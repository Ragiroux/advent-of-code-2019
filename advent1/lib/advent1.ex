defmodule Advent1 do

  ############
  # PART 1
  ############
  def main do
    readFile
    |> Enum.map(&IO.inspect(&1))
    |> Enum.map(&(&1/3))
    |> Enum.map(&Float.floor(&1, 0))
    |> Enum.map(&(&1 - 2))
    |> Enum.map(&IO.inspect(&1))
    |> Enum.sum
  end

  ############
  # PART 2
  ############
  def part2 do

    fuel = readFile
    |> Enum.map(&calculateFuel(&1) - &1)
    |> Enum.sum

    IO.puts "Fuel for santa #{fuel}"

    fuel

  end

  def calculateFuel(mass) when mass <= 0, do: 0

  def calculateFuel(mass) do
    mass + calculateFuel( Float.floor(mass / 3, 0) - 2)
  end

  def readFile do
    File.stream!("input.txt")
    |> Stream.map( &(String.replace(&1, "\n", "")) )
    |> Enum.map(&String.to_integer/1)
  end
end

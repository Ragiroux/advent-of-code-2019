defmodule Advent1 do

  def main do
    readFile
    |> Enum.map(&IO.inspect(&1))
    |> Enum.map(&(&1/3))
    |> Enum.map(&Float.floor(&1, 0))
    |> Enum.map(&(&1 - 2))
    |> Enum.map(&IO.inspect(&1))
    |> Enum.sum
  end

  def readFile do
    File.stream!("input.txt")
    |> Stream.map( &(String.replace(&1, "\n", "")) )
    |> Enum.map(&String.to_integer/1)
  end
end

defmodule Advent2Part2 do

  def part2 do
   readFile() |> calculateOptCode(0,0)
  end

  def calculateOptCode(operation, optCode, pointer) when optCode == 99 do
    IO.inspect operation
    result = operation |> Enum.at(0)
    cond do
      result == 19690720 -> operation
      true -> readFile() |> List.delete_at(1)  |> List.insert_at(1, :rand.uniform(100)) |>  List.delete_at(2)  |> List.insert_at(2, :rand.uniform(100)) |> calculateOptCode(0,0)
    end
  end

  def calculateOptCode(operation, optCode, pointer) do

    optCode = operation |> Enum.at(pointer)

    cond do
      optCode == 1 -> optCode1(operation, pointer)
      optCode == 2 -> optCode2(operation, pointer)
      optCode == 99 -> calculateOptCode(operation, 99, pointer)
    end
  end

  def optCode1(operation, pointer) do
    ia =  operation |> Enum.at(pointer + 1)
    ib = operation |> Enum.at(pointer + 2)
    dest = operation |> Enum.at(pointer + 3)
    va = operation |> Enum.at(ia)
    vb = operation |> Enum.at(ib)
    operation |> List.delete_at(dest) |> List.insert_at(dest, va+vb) |> calculateOptCode(1, pointer + 4)
  end

  def optCode2(operation, pointer) do
    ia =  operation |> Enum.at(pointer + 1)
    ib = operation |> Enum.at(pointer + 2)
    dest = operation |> Enum.at(pointer + 3)
    va = operation |> Enum.at(ia)
    vb = operation |> Enum.at(ib)
    operation |> List.delete_at(dest) |> List.insert_at(dest, va*vb) |> calculateOptCode(2, pointer + 4)
  end

  def readFile do
    File.read!("input.txt")
    |> String.split(",")
    |> Enum.map(&(String.to_integer(&1)))
  end
end


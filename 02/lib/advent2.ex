defmodule Advent2 do

  def part1 do
   readFile() |> calculateOptCode(0,0)
  end

  def calculateOptCode(operation, optCode, pointer) when optCode == 99, do: operation

  def calculateOptCode(operation, optCode, pointer) do

    optCode = operation |> Enum.at(pointer)
    IO.puts "OptCode = #{optCode} pointer = #{pointer}"
    IO.inspect operation

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
    IO.puts "ia: #{ia}; va: #{va}, ib: #{ib}, vb: #{vb}, dest: #{dest}"
    operation |> List.delete_at(dest) |> List.insert_at(dest, va+vb) |> IO.inspect |> calculateOptCode(1, pointer + 4)
  end

  def optCode2(operation, pointer) do
    ia =  operation |> Enum.at(pointer + 1)
    ib = operation |> Enum.at(pointer + 2)
    dest = operation |> Enum.at(pointer + 3)
    va = operation |> Enum.at(ia)
    vb = operation |> Enum.at(ib)
    IO.puts "ia: #{ia}; va: #{va}, ib: #{ib}, vb: #{vb}, dest: #{dest}"
    operation |> List.delete_at(dest) |> List.insert_at(dest, va*vb) |> IO.inspect |> calculateOptCode(2, pointer + 4)
  end

  def readFile do
    File.read!("input.txt")
    |> String.split(",")
    |> Enum.map(&(String.to_integer(&1)))
  end
end

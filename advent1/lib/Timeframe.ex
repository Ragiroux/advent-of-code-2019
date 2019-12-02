defmodule Timeframe do
  defmacro execute(name, units \\ :millisecond, do: yield) do
    quote do
      start = System.monotonic_time(unquote(units))
      result = unquote(yield)
      time_spent = System.monotonic_time(unquote(units)) - start
      IO.puts("Executed #{unquote(name)} in #{time_spent} #{unquote(units)}")
      result
    end
  end
end

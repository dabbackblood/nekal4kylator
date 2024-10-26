#ДАНОЕ ПРИЛОЖЕНИЕ РАЗРАБОТАНО Ghost
import math
import random
v = "⎸"
m = "╲"
c = "/"
h = "╲"
j = "-"

print(f"                                                                                                                                                          ____")
print(f"{v}  {c}      {c} {h}               {c}{h}        {v}  {c}    {h}       {c}      {c}{h}             ╭_________                __________               (☷☷☷☷☷☷)                {v}   {v}—————————{v}")
print(f"{v} {c}      {c}    {h}            {c}  {h}       {v} {c}       {h}    {c}      {c}  {h}            {v}        {v}                     {v}                   (         )                {v}  {v}          {v}")
print(f"{v}{c}      {c}      {h}          {c}    {h}      {v}{c}          {h} {c}      {c}    {h}           {v}        {v}                     {v}                   (         )                {v}  {v}——————————{v}")
print(f"{v}{h}     {c}---------{h}       {c}      {h}     {v}{h}           {v}      {c}      {h}          {v}________{v}                     {v}                   (         )                {v}  {v}")
print(f"{v} {h}   {c}           {h}     {c}        {h}    {v}  {h}         {v}     {c}        {h}        {c}         {v}                     {v}                   (         )                {v}  {v}")
print(f"                                                   {v}                      {c}          {v}                     {v}                   ╰◡◡◡◡◡◡◡)               {v}  {v}")
print(f"                                                                         {c}           {v}                                                                    ———")
from colorama import init
from colorama import  Fore, Back, Style
init()
print
print(Fore.GREEN)
a = float(input("Ведите первое число:"))
b = float(input("Ведите второе число:"))

operation = input("Что сделать? (+,-,*,/): ")
result = 0

if operation == "+":
    result = a + b
elif operation == "-":
    result = a-b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
    print(Fore.YELLOW)
print(f"Результат: {result}")

input()
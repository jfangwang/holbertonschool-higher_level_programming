score=0
task=0
#task 0 and 1

if grep -q "type" 0-answer.txt; then
    ((score++))
    ((task++))
else
    echo "Task is wrong"
fi

if grep -q "id" 0-answer.txt; then
    ((score++))
    ((task++))
else
    echo Task ${task} is wrong
fi

#task
index=0
max=28
python << END
#!/usr/bin/python
import subprocess

a = 89
b = 100
if a is b:
    echo Task ${task} is wrong
else:
    subprocess.call(["(($score++))"])
END
echo $score

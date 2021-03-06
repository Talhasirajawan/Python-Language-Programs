{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A': 1, 'B': 1, 'C': 1, 'D': 1}\n",
      "Vaccum is randomly select to C\n",
      "Moving to Location D...\n",
      "D is dirty\n",
      "Location D has been Cleaned.\n",
      "Moving to Location C...\n",
      "C is dirty\n",
      "Location C has been Cleaned.\n",
      "Moving to Location B...\n",
      "B is dirty\n",
      "Location B has been Cleaned.\n",
      "Moving to Location A...\n",
      "A is dirty\n",
      "Location A has been Cleaned.\n",
      "{'A': 0, 'B': 0, 'C': 0, 'D': 0}\n",
      "Performance Measurement: 0\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "class Environment(object):\n",
    "    def __init__(self):\n",
    "        self.places={'A':'0','B':'0','C':'0','D':'0'}\n",
    "        self.places['A']=1\n",
    "        self.places['B']=1\n",
    "        self.places['C']=1\n",
    "        self.places['D']=1\n",
    "class Agent(Environment):\n",
    "    def __init__(self,Environment):\n",
    "        print(Environment.places)\n",
    "        Score=0\n",
    "        Location = 2\n",
    "        if Location == 0:\n",
    "            print(\"Vaccum is randomly select to A\")\n",
    "            if Environment.places['A'] == 1:\n",
    "                print(\"A is dirty\")\n",
    "                Environment.places['A']=0\n",
    "                Score=+1\n",
    "                print(\"Location A has been Cleaned.\")\n",
    "                # move to B\n",
    "                print(\"Moving to Location B...\")\n",
    "                Score -= 1\n",
    "            if Environment.places['B'] == 1:\n",
    "                print(\"B is dirty\")\n",
    "                Environment.places['B']=0\n",
    "                Score=+1\n",
    "                print(\"Location B has been Cleaned.\")\n",
    "                # move to B\n",
    "                print(\"Moving to Location C...\")\n",
    "                Score -= 1\n",
    "            if Environment.places['C'] == 1:\n",
    "                print(\"C is dirty\")\n",
    "                Environment.places['C']=0\n",
    "                Score=+1\n",
    "                print(\"Location C has been Cleaned.\")\n",
    "                Score -= 1\n",
    "            if Environment.places['D'] == 1:\n",
    "                    print(\"D is dirty\")\n",
    "                    Environment.places['D']=0\n",
    "                    Score=+1\n",
    "                    print(\"Location D has been Cleaned.\")\n",
    "\n",
    "        else:\n",
    "            if Location == 1:\n",
    "                print(\"Vaccum is randomly select to B\")\n",
    "                if Environment.places['A'] == 1:\n",
    "                    print(\"A is dirty\")\n",
    "                    Environment.places['A']=0\n",
    "                    Score=+1\n",
    "                    print(\"Location A has been Cleaned.\")\n",
    "                    # move to B\n",
    "                    print(\"Moving to Location B...\")\n",
    "                    Score -= 1\n",
    "                if Environment.places['B'] == 1:\n",
    "                    print(\"B is dirty\")\n",
    "                    Environment.places['B']=0\n",
    "                    Score=+1\n",
    "                    print(\"Location B has been Cleaned.\")\n",
    "                    # move to B\n",
    "                    print(\"Moving to Location C...\")\n",
    "                    Score -= 1\n",
    "                if Environment.places['C'] == 1:\n",
    "                    print(\"C is dirty\")\n",
    "                    Environment.places['C']=0\n",
    "                    Score=+1\n",
    "                    print(\"Location C has been Cleaned.\")\n",
    "                    Score -= 1\n",
    "                if Environment.places['D'] == 1:\n",
    "                    print(\"D is dirty\")\n",
    "                    Environment.places['D']=0\n",
    "                    Score=+1\n",
    "                    print(\"Location D has been Cleaned.\")\n",
    "                    # move to B\n",
    "            else:\n",
    "                if Location == 2:\n",
    "                    print(\"Vaccum is randomly select to C\")\n",
    "                    if Environment.places['D'] == 1:\n",
    "                        print(\"Moving to Location D...\")\n",
    "                        print(\"D is dirty\")\n",
    "                        Environment.places['D']=0\n",
    "                        Score=+1\n",
    "                        print(\"Location D has been Cleaned.\")\n",
    "                        # move to B\n",
    "                        print(\"Moving to Location C...\")\n",
    "                    if Environment.places['C'] == 1:\n",
    "                        print(\"C is dirty\")\n",
    "                        Environment.places['C']=0\n",
    "                        Score=+1\n",
    "                        print(\"Location C has been Cleaned.\")\n",
    "                    # move to B\n",
    "                        print(\"Moving to Location B...\")\n",
    "                        Score -= 1\n",
    "                    if Environment.places['B'] == 1:\n",
    "                        print(\"B is dirty\")\n",
    "                        Environment.places['B']=0\n",
    "                        Score=+1\n",
    "                        print(\"Location B has been Cleaned.\")\n",
    "                        # move to B\n",
    "                        print(\"Moving to Location A...\")\n",
    "                        Score -= 1\n",
    "                    if Environment.places['A'] == 1:\n",
    "                        print(\"A is dirty\")\n",
    "                        Environment.places['A']=0\n",
    "                        Score=+1\n",
    "                        print(\"Location A has been Cleaned.\")\n",
    "                        Score -= 1\n",
    "                    else:\n",
    "                        print(\"Vaccum is randomly select to D\")\n",
    "                        if Environment.places['D'] == 1:\n",
    "                            print(\"D is dirty\")\n",
    "                            Environment.places['D']=0\n",
    "                            Score=+1\n",
    "                            print(\"Location D has been Cleaned.\")\n",
    "                            # move to B\n",
    "                            print(\"Moving to Location C...\")\n",
    "                            Score -= 1\n",
    "                        if Environment.places['C'] == 1:\n",
    "                            print(\"C is dirty\")\n",
    "                            Environment.places['C']=0\n",
    "                            Score=+1\n",
    "                            print(\"Location C has been Cleaned.\")\n",
    "                            # move to B\n",
    "                            print(\"Moving to Location B...\")\n",
    "                            Score -= 1\n",
    "                        if Environment.places['B'] == 1:\n",
    "                            print(\"B is dirty\")\n",
    "                            Environment.places['B']=0\n",
    "                            Score=+1\n",
    "                            print(\"Location B has been Cleaned.\")\n",
    "                            # move to B\n",
    "                            print(\"Moving to Location A...\")\n",
    "                            Score -= 1\n",
    "                        if Environment.places['A'] == 1:\n",
    "                            print(\"A is dirty\")\n",
    "                            Environment.places['A']=0\n",
    "                            Score=+1\n",
    "                            print(\"Location A has been Cleaned.\")\n",
    "                            Score -= 1\n",
    "        print (Environment.places)\n",
    "        print (\"Performance Measurement: \" + str(Score))\n",
    "    \n",
    "theEnvironment = Environment()\n",
    "theVacuum = Agent(theEnvironment)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

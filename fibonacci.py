{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-14-02a510a9da12>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-14-02a510a9da12>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    if n<0:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "n=input(\"Enter number: \")\n",
    "Fibonacci(n)\n",
    "    if n<0: \n",
    "        print(\"Incorrect input\") \n",
    "    elif n==1: \n",
    "        return 0\n",
    "    elif n==2: \n",
    "        return 1\n",
    "    else: \n",
    "        return Fibonacci(n-1)+Fibonacci(n-2) \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "144\n"
     ]
    }
   ],
   "source": [
    "def Fibonacci(n): \n",
    "    if n<0: \n",
    "        print(\"Incorrect input\") \n",
    "    elif n==1: \n",
    "        return 0 \n",
    "    elif n==2: \n",
    "        return 1\n",
    "    else: \n",
    "        return Fibonacci(n-1)+Fibonacci(n-2) \n",
    "print(Fibonacci(13)) \n",
    "\n"
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

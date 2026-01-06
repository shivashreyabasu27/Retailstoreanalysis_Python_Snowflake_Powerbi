{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e81cf236-aaff-4b18-93d5-74faf66e02ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1703b387-02fc-4a4e-8eea-22a46f18a1ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "n= pd.read_csv(\"samplecsv.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cd1dd10f-1c44-4300-aacf-e7f35d7d999d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>New York</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>Los Angeles</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age         City \n",
       "0    Alice   25     New York \n",
       "1      Bob   30  Los Angeles \n",
       "2  Charlie   35       Chicago"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3b74fc64-996c-41ea-a783-209f628366a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age    City \n",
       "2  Charlie   35  Chicago"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n.tail(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0740a6ed-9db6-4aca-9435-97edefa74b06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>27.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>32.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Age\n",
       "count   3.0\n",
       "mean   30.0\n",
       "std     5.0\n",
       "min    25.0\n",
       "25%    27.5\n",
       "50%    30.0\n",
       "75%    32.5\n",
       "max    35.0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4eb5d6ec-72ca-45c9-a320-93a7cfca692a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Name     object\n",
       "Age       int64\n",
       "City     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "352d7d8a-00f5-491c-a1a9-1d2dabd92653",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      Alice\n",
       "1        Bob\n",
       "2    Charlie\n",
       "Name: Name, dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n['Name']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d68f4a7c-9415-4dd3-afad-5a3edf8171c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Name      True\n",
       "Age      False\n",
       "City      True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n.dtypes==object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3f5c06ed-5c9a-41f7-a57f-d45eebf951da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age\n",
       "1      Bob   30\n",
       "2  Charlie   35"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n[['Name','Age']][1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "114521a7-86dc-4b41-898a-00c7284f7520",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age         City   new\n",
       "0    Alice   25     New York   hyd\n",
       "1      Bob   30  Los Angeles   hyd\n",
       "2  Charlie   35       Chicago  hyd"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n['new']='hyd'\n",
    "n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "15fdc074-7611-4228-a428-6421a1564d95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>in</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Name  Age  in      City   new\n",
       "0  Alice   25   0  New York   hyd"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n[0:1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8731f53e-c8da-42bf-bdc9-82af4675c3ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "a= n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2062931c-4daf-40ba-bf4b-8c1f64e84f52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>in</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  in         City   new\n",
       "0    Alice   25   0     New York   hyd\n",
       "1      Bob   30   0  Los Angeles   hyd\n",
       "2  Charlie   35   0       Chicago  hyd"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "791a0543-aa1e-42a7-86b4-0ca987448320",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "33e1b057-7f46-470c-a7b3-4b1243ce94a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "i=[101,201,301,401,501]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d75c0515-ac85-494f-995f-3a1d37951599",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>Name</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>201</th>\n",
       "      <td>Age</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>301</th>\n",
       "      <td>in</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>401</th>\n",
       "      <td>City</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>501</th>\n",
       "      <td>new</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         0\n",
       "101   Name\n",
       "201    Age\n",
       "301     in\n",
       "401  City \n",
       "501    new"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(list(a),index = i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "9ade88bd-965d-4b24-954f-a8e909063184",
   "metadata": {},
   "outputs": [],
   "source": [
    "a.drop('in',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "059662a8-56c4-4790-998b-6dea1c2ecdfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age         City   new\n",
       "0    Alice   25     New York   hyd\n",
       "1      Bob   30  Los Angeles   hyd\n",
       "2  Charlie   35       Chicago  hyd"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "928f23e0-09fb-472c-8cd7-5b7ca8074de6",
   "metadata": {},
   "outputs": [],
   "source": [
    "a.set_index('Name', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "ab03ee71-a8d9-4e52-98fb-b7d3258ae68e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Alice</th>\n",
       "      <td>25</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Bob</th>\n",
       "      <td>30</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Charlie</th>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Age         City   new\n",
       "Name                           \n",
       "Alice     25     New York   hyd\n",
       "Bob       30  Los Angeles   hyd\n",
       "Charlie   35       Chicago  hyd"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "8c3758ab-c161-4011-9120-bc68132304bf",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>City</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>New York</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>hyd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age         City   new\n",
       "0    Alice   25     New York   hyd\n",
       "1      Bob   30  Los Angeles   hyd\n",
       "2  Charlie   35       Chicago  hyd"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "e8243b5c-7014-4c2e-818f-5a12c06eb24e",
   "metadata": {},
   "outputs": [],
   "source": [
    "b={ 'key1':[1,2,3],'key2':[4,5,6]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "fb16a08d-be4d-4c07-8104-02674d36ee10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'key1': [1, 2, 3], 'key2': [4, 5, 6]}\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "292633b3-5f45-4b17-b963-3213f70352f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key1</th>\n",
       "      <th>key2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   key1  key2\n",
       "0     1     4\n",
       "1     2     5\n",
       "2     3     6"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "ab5ea23d-6ba5-4ae6-8b71-81da0dd99c10",
   "metadata": {},
   "outputs": [],
   "source": [
    "n.to_csv('newdata.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "237b55c2-0e0a-42fa-bb11-7649b1940f0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shape:(3, 3)\n",
      "columns:Index(['Age', 'City ', 'new'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(f'shape:{n.shape}')\n",
    "print(f'columns:{n.columns}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "690527ee-3a92-4f96-b0ad-a342222c1f3b",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'Name'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mFile \u001b[39m\u001b[32m/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/pandas/core/indexes/base.py:3812\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3811\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m3812\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_engine\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcasted_key\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   3813\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/index.pyx:167\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/index.pyx:196\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/hashtable_class_helper.pxi:7088\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/hashtable_class_helper.pxi:7096\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[31mKeyError\u001b[39m: 'Name'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[93]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m n[(n[\u001b[33m'\u001b[39m\u001b[33mAge\u001b[39m\u001b[33m'\u001b[39m]>\u001b[32m25\u001b[39m)&(\u001b[43mn\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mName\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m==\u001b[33m'\u001b[39m\u001b[33mBob\u001b[39m\u001b[33m'\u001b[39m)]\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/pandas/core/frame.py:4113\u001b[39m, in \u001b[36mDataFrame.__getitem__\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   4111\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m.columns.nlevels > \u001b[32m1\u001b[39m:\n\u001b[32m   4112\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m._getitem_multilevel(key)\n\u001b[32m-> \u001b[39m\u001b[32m4113\u001b[39m indexer = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   4114\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m is_integer(indexer):\n\u001b[32m   4115\u001b[39m     indexer = [indexer]\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/opt/conda/envs/anaconda-2025.12-py312/lib/python3.12/site-packages/pandas/core/indexes/base.py:3819\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3814\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(casted_key, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;129;01mor\u001b[39;00m (\n\u001b[32m   3815\u001b[39m         \u001b[38;5;28misinstance\u001b[39m(casted_key, abc.Iterable)\n\u001b[32m   3816\u001b[39m         \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28many\u001b[39m(\u001b[38;5;28misinstance\u001b[39m(x, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;28;01mfor\u001b[39;00m x \u001b[38;5;129;01min\u001b[39;00m casted_key)\n\u001b[32m   3817\u001b[39m     ):\n\u001b[32m   3818\u001b[39m         \u001b[38;5;28;01mraise\u001b[39;00m InvalidIndexError(key)\n\u001b[32m-> \u001b[39m\u001b[32m3819\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01merr\u001b[39;00m\n\u001b[32m   3820\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m:\n\u001b[32m   3821\u001b[39m     \u001b[38;5;66;03m# If we have a listlike key, _check_indexing_error will raise\u001b[39;00m\n\u001b[32m   3822\u001b[39m     \u001b[38;5;66;03m#  InvalidIndexError. Otherwise we fall through and re-raise\u001b[39;00m\n\u001b[32m   3823\u001b[39m     \u001b[38;5;66;03m#  the TypeError.\u001b[39;00m\n\u001b[32m   3824\u001b[39m     \u001b[38;5;28mself\u001b[39m._check_indexing_error(key)\n",
      "\u001b[31mKeyError\u001b[39m: 'Name'"
     ]
    }
   ],
   "source": [
    "n[(n['Age']>25)&(n['Name']=='Bob')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f050b309-cc1c-4df1-8a26-e580a1f1c2bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2025.12-py312",
   "language": "python",
   "name": "conda-env-anaconda-2025.12-py312-py"
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
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

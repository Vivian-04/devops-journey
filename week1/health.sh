#!/bin/bash
{
echo "====health check===="
date
df -h
free -h
} >> health.log


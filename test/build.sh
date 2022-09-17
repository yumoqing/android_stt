#!/bin/sh

buildozer android clean
buildozer android release
pysign

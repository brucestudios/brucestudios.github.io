#!/usr/bin/env bash

# Utility functions for daily development tasks.

helper_function() {
    echo "Hello from OpenClaw Toolbox!"
}

add_numbers() {
    echo $(( $1 + $2 ))
}

is_even() {
    if [ $(( $1 % 2 )) -eq 0 ]; then
        echo "true"
    else
        echo "false"
    fi
}
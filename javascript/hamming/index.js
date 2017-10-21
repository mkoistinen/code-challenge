/**
 * Hamming distance, copyright (c) 2017 My Employer, All rights reserved.
 * Author: Martin Koistinen
 * */

var Hamming = function(){
    'use strict';

    this.compute = function(stringA, stringB) {
        //
        // Computes the Hamming distance of the two given strings
        //
        var position, distance = 0;

        if (stringA.length !== stringB.length) {
            throw 'DNA strands must be of equal length.';
        }

        // NOTE: The provided reference link to Rosalind suggests that the
        // given two strings will not exceed 1kbp. However, I did not find this
        // to be a theoretical restriction of any sort in my brief research,
        // so, I assume this is merely a note to test-takers about the size
        // they should plan for and not a test requirement. Otherwise, I would
        // just issue a warning when `length` exceeds 1000.

        for (position=0; position<stringA.length; position++) {
            if (stringA[position] !== stringB[position]) {
                distance += 1;
            }
        }

        return distance;
    }
};

module.exports = Hamming;

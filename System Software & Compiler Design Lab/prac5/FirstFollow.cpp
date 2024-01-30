// To find First and Follow set of a given grammar

#include <bits/stdc++.h>
#include <map>
#include <vector>
#include <set>
using namespace std;


//map for first set of all Rules (of all heads)
map<string, set<char>> firstSet;

//map for follow set of all Rules (of all heads)
map<string, set<char>> followSet;

//map for grammar rules
//it stores alphabetic wise by default
map <string, set<string>> m = {
    {"A",{"a","^"}},
    {"B", {"b"}},
    {"S", {"aAb", "B"}}
};




//function that calculates the first set for an element, stores it in fs & returns it.
set<char> calculateFirst(string head, set<string> v){
    set<char> fs;
    
    // traversing list (rules) for the head variable
    for (auto j : v){
        char firstLetterOfRule = j[0];

        if (islower(firstLetterOfRule) || firstLetterOfRule == '^'){
            fs.insert(firstLetterOfRule);
        }

        else{
            string newHead = "";
            newHead +=firstLetterOfRule;

            set<string> newSet = m[newHead];
            
            set<char> tempSet = calculateFirst(newHead, newSet);
            for (auto i : tempSet){
                fs.insert(i);
            }
        }
    }
    return fs;
}

//function that calculates the follow set
void calculateFollow(string LHS, set<string> RHS){
    
    // traversing list (rules) for the head variable
    for (auto rule : RHS){
        int ruleTraverser = 0;
        int ruleLength = rule.length();
        
        while (ruleTraverser < ruleLength){
            if (isupper(rule[ruleTraverser])){

                //saving current character to a variable
                char tempHead = rule[ruleTraverser];
                string header = "";
                header += tempHead;

                //checking if it is the last character of the rule, in which case, we will take Follow of LHS
                if (ruleTraverser == ruleLength-1){

                    set<char> tempSet = followSet[LHS];
                    //now this will be the follow set of the character too
                    for (auto ele : tempSet){
                        followSet[header].insert(ele);
                    }
                }
                else{
                    //if the next character is a terminal (lowercase), simply add it to the Follow set
                    if (islower(rule[ruleTraverser+1])){

                        followSet[header].insert(rule[ruleTraverser+1]);
                    }
                    //if the next character is also a variable (uppercase), then its First will be the Follow set
                    else {
                        char nextCharacter0 = rule[ruleTraverser+1];
                        string nextCharacter = "";
                        nextCharacter += nextCharacter0;

                        set<char> tempSet = firstSet[nextCharacter];
                        //now this will be follow set of the character
                        for (auto ele :tempSet){
                            followSet[header].insert(ele);
                        }
                    }
                }
            }
            ruleTraverser++;
        }
        
    }
}

int main(){

    //initializing iterator for map
    map<string, set<string>>:: iterator i;

    //calculating First set
    for (i=m.begin(); i!= m.end(); i++){
        set<char> fs = calculateFirst(i->first, i->second);
        // insert this first set into map of firstSet
        firstSet[i->first] = fs;
    }

    //calculating Follow set
    followSet["S"].insert('$');     //since start symbol's follow set always has '$'
    for (i=m.begin(); i!= m.end(); i++){
        calculateFollow(i->first, i->second);
    }


    //printing the first set
    cout<<"The Follow Set of each variable is: \n";
    map<string, set<char>>:: iterator it;
    for (it=firstSet.begin(); it!= firstSet.end(); it++){
        string head = it->first;
        cout<<head<<": ";
        for (auto ele : it->second){
            cout<<ele;
            if (ele != *prev(it->second.end())){
                cout<<",";
            }
        }
        cout<<endl;
    }
    cout<<endl;


    //printing the follow set
    cout<<"The Follow Set of each variable is: \n";
    map<string, set<char>>:: iterator it2;
    for (it2=followSet.begin(); it2!= followSet.end(); it2++){
        string head = it2->first;
        cout<<head<<": ";
        for (auto ele : it2->second){
            cout<<ele;
            if (ele != *prev(it2->second.end())){
                cout<<",";
            }
        }
        cout<<endl;
    }

    return 0;
}
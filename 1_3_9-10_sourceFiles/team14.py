####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

x = 6
y = 0
z = 0
team_name = 'E3'
strategy_name = 'Collude but retaliate'
strategy_description = '''\
Collude first round. Collude, except in a round after getting 
a severe punishment.'''
Choice =0
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history) < 51:
        if len(my_history)==4: # It's the first round; collude.
            return 'b'
        elif len(my_history) < 10:
            return 'c'
        elif their_history[5] == 'b':
            if their_history[their_history < 10 and not 5] == "c":
                if len(my_history) == 49:
                    return 'b'
                else: return 'c'
                
            elif their_history[their_history < 6] == "c" and their_history[5 < their_history and their_history <11] == "b":
                return "b"
            
            else:
                for l in Bigg:
                    if their_history[x] == "b":
                        y += 1
                        x += 1
                    else:
                        z += 0
                    x = 6
                if y < 3:
                    if len(my_history) == 49:
                        return "b"
                    else:
                        return "c"
                else:
                    return "b"
        else:
            return "c"
    
    elif len(my_history) < 101:
        if len(my_history)==54: # It's the first round; collude.
            return 'b'
        elif len(my_history) < 60:
            return 'c'
        elif their_history[55] == 'b':
            if their_history[their_history < 60 and not 55] == "c":
                if len(my_history) == 99:
                    return 'b'
                else: return 'c'
                
            elif their_history[51 < their_history and their_history <56] == "c" and their_history[55 < their_history and their_history <61] == "b":
                return "b"
            
            else:
                for l in Bigg:
                    if their_history[x] == "b":
                        y += 1
                        x += 1
                    else:
                        z += 0
                    x = 6
                if y < 3:
                    if len(my_history) == 99:
                        return "b"
                    else:
                        return "c"
                else:
                    return "b"
    else:
        return "c"
    if their_history[98] == 'c':
        return 'c'
    else:
        return 'b'
#up bois
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             

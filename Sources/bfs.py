import support_function as spf
import time

'''
//========================//
//           BFS          //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''
def BFS_search(board, list_check_point):
    start_time = time.time()
    ''' BFS SEARCH SOLUTION '''
    ''' IF START BOARD IS GOAL OR DON'T HAVE CHECK POINT '''
    if spf.check_win(board,list_check_point):
        print("Found win")
        return [board]

    ''' INITIALIZE START STATE '''
    start_state = spf.state(board, None, list_check_point)
    ''' INITIALIZE 2 LISTS USED FOR BFS SEARCH '''
    list_state = [start_state]
    list_visit = [start_state]
    ''' LOOP THROUGH VISITED LIST '''
    while len(list_visit) != 0:
        ''' GET NOW STATE TO SEARCH '''
        now_state = list_visit.pop(0)

        for row in now_state.board:
            print(' '.join(row))
        print("\n")
        ''' GET THE PLAYER'S CURRENT POSITION '''
        cur_pos = spf.find_position_player(now_state.board)


        ''' GET LIST POSITION THAT PLAYER CAN MOVE TO '''
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)
        ''' MAKE NEW STATES FROM LIST CAN MOVE '''
        for next_pos in list_can_move:
            ''' MAKE NEW BOARD '''
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)
            ''' IF THIS BOARD DON'T HAVE IN LIST BEFORE --> SKIP THE STATE '''
            if spf.is_board_exist(new_board, list_state):
                continue
            ''' IF ONE OR MORE BOXES ARE STUCK IN THE CORNER --> SKIP THE STATE '''
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue
            ''' IF ALL BOXES ARE STUCK --> SKIP THE STATE '''
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' MAKE NEW STATE '''
            new_state = spf.state(new_board, now_state, list_check_point)
            ''' CHECK WHETHER THE NEW STATE IS GOAL OR NOT '''
            if spf.check_win(new_board, list_check_point):
                print("Found win")
                print("States:", len(list_state))
                print("Time:", time.time() - start_time)
                return (new_state.get_line(), len(list_state))
            
            ''' APPEND NEW STATE TO VISITED LIST AND TRAVERSED LIST '''
            list_state.append(new_state)
            list_visit.append(new_state)

            ''' COMPUTE THE TIMEOUT '''
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []
        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []
    ''' SOLUTION NOT FOUND '''
    print("Not Found")
    return []
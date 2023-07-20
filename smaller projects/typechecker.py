def check_structure(object,description):
    stack=[(object,description,[])]
    while len(stack)!=0:
        (cur_obj,cur_desc,cur_path)=stack.pop()
        if type(cur_desc) == type:
            if type(cur_obj)!=cur_desc:
                return False,cur_path
        else:
            cur_type=cur_desc[0]
            cur_subtype=cur_desc[1]
            if type(cur_obj)!=cur_type:
                return False,cur_path
            if type(cur_obj)==list:
                for i in range(len(cur_obj)):
                    stack.append((cur_obj[i],cur_subtype,cur_path+[i]))
            elif type(cur_obj)==dict:
                for (e,v) in cur_obj:
                    stack.append((e,cur_subtype[0],cur_path+[e]))
                    stack.append((v,cur_subtype[1],cur_path+[v]))
    return True


def test1():
    if not check_structure(1,int)==True:
        return False
    if not check_structure(1,str)==False:
        return False
    return True

def test2():
    object=[1,2,3]
    description=(list,[int,str])




def main():
    print(test1())
    return


if __name__ == "__main__":
    main()

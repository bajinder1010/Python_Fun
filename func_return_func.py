def grumpy():
    print("I am a grumpy cat:")
    def no_n_times(n):
            print("No", n,"times...")
            def no_m_more_times(m):
                    print("...and no", m,"more times")
                    for i in range(n+m):
                     print("no")
            return no_m_more_times
    return no_n_times

grumpy()(4)(2)
/* 
 * File:   AmplifierDriver.h
 * Author: Macias
 *
 * Created on 14 październik 2010, 16:25
 */

#ifndef AMPLIFIERDRIVER_H
#define	AMPLIFIERDRIVER_H
#include <vector>
#include <stdlib.h>
#include <ctime>
using namespace std;
class AmplifierDriver
{
protected:
    bool sampling;
    int sampling_rate;
    vector<int> active_channels;
    clock_t last_sample;
public:
    AmplifierDriver(){};
    virtual void start_sampling()
    {
        sampling=true;
    }
    virtual void stop_sampling()
    {
        sampling=false;
    }
    virtual int fill_samples(vector<int> &samples)
    {   if (!sampling) return -1;
        for (unsigned int i=0;i<active_channels.size();i++)
            samples[i]=rand();
    synchronize();
    return active_channels.size();
    }
    virtual int fill_samples(vector<float> &samples)
    {   if (!sampling) return -1;
        for (unsigned int i=0;i<active_channels.size();i++)
            samples[i]=((float)rand())/RAND_MAX;
    synchronize();
    return active_channels.size();
    }
    virtual void set_active_channels(vector<int> &channels)
    {
        active_channels = channels;
    }
    inline bool is_sampling(){return sampling;}
    virtual int set_sampling_rate(int samp_rate)
    {
        return sampling_rate=samp_rate;
    }
    virtual int get_sampling_rate()
    {return sampling_rate;}
private:
    void synchronize()
    {
    clock_t this_sample=clock();
    float wait= (1.0/sampling_rate)-(this_sample-last_sample)/CLOCKS_PER_SEC;
    if (wait>0)
        usleep((int)(wait*1000000));
    last_sample=this_sample;
    }
};



#endif	/* AMPLIFIERDRIVER_H */

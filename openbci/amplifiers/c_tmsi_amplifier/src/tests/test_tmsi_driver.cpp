/*
 * File:   test_driver.cpp
 * Author: Macias
 *
 * Created on 2010-10-19, 16:06:44
 */

#include "../TmsiAmplifier.h"
#include "test_driver.h"

int main(int argc,char** argv){
	TmsiAmplifier amp;
	test_driver(argc,argv,&amp);
}

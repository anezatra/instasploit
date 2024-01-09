#############################################################
# Instasploit v1.0
# Title: instasploit instagram deep exploration tool
# Author: Anezatra Katedram
# System request: Linux Version(Debian/Ubuntu) and Win64/32
# Terminal: Linux
# Description: Instagram deep knowledge gathering
# Last update: 9/01/2024 Bugs fixed
# Generated: -
#############################################################

import os
import re
import sys
import random
import pygame
import colorama
import requests
import platform
import datetime
import itertools
import threading
import instaloader
import time

from getpass import getpass
from colorama import Fore, Back, Style
from instaloader import Instaloader, Profile

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def play_alert_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/alert.mp3")
    pygame.mixer.music.play()

def play_start_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/start.mp3")
    pygame.mixer.music.play()

def play_command():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/command.mp3")
    pygame.mixer.music.play()
      
def shell():
   
   print("\n================================================================== ")
   print("                     PLEASE ENTER CREDENTIALS                        ")     
   print("==================================================================   ")
   username = input("\n[*] Username: ")
   password = getpass("[*] Password: ")
   time.sleep
   try:
     print("[*] Trying to login...")
     L = instaloader.Instaloader()
     L.context.login(username, password)
     print("\n[+] Logged as: " + username + " Method: Instaloader [SUCCESS]")

   except instaloader.exceptions.BadCredentialsException:
     print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
     print("[-] Please restart the program or check your password.\n")
     play_alert_sound()
     time.sleep(10)
     os_shell()
    
   except instaloader.exceptions.LoginRequiredException as e:
    
    if str(e).startswith("Login error: \"fail\""):
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("[-] Sorry, your password was incorrect. Please double-check your password.\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    if str(e.code) == '501':
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("[-] Instagram server is currently down\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '404':
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("[-] The page was not found or does not exist\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '503':
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("[-] Instagram server is currently unavailable.\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '403':
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("\n[-] Too many requests, please try again later.\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    else:
        print("\n[-] Not Logged as: " + username + " Method: Instaloader [ERROR]")
        print("[-] Error code:", e.code, "\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()


   target = input("\n[*] Target username: ")
   print("\n[*] Connecting to: https://instagram.com/" + target + "/...")
   try:
    profile = instaloader.Profile.from_username(L.context, target)
    response = requests.get(f"https://www.instagram.com/{target}/")
    total_sent_bytes = len(response.content)
    for i in range(total_sent_bytes):
         print(f"[*] Sending stage {i + 1} of {total_sent_bytes} bytes...", end='\r')
         time.sleep(0.0000001)
   except instaloader.exceptions.ProfileNotExistsException:
    print("[-] Connection failure: no target or server error")
    print(f"[-] Login completed, but the command shell could not be opened\n")
    play_alert_sound()
    time.sleep(10)
    os_shell()
   except instaloader.exceptions.HTTPException as e:
    if str(e.code) == '501':
        print("[-] Connection failure: Instagram server is currently down")
        print(f"[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '404':
        print("[-] Connection failure: The page was not found or does not exist")
        print("[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '503':
        print("[-] Connection failure: Ignstagram server is currently unavailable")
        print("[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '403':
        print("[-] Connection failure: Too many request, please try again later") 
        print("[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    elif str(e.code) == '401':
        print("[-] Connection failure: Unauthorized method, please check your account") 
        print("[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
    else:
        print("[-] Connection failure: connection closed for unknown reason")
        print("[-] Error code:", e.code, "\n")
        print("[-] Login completed, but the command shell could not be opened\n")
        play_alert_sound()
        time.sleep(10)
        os_shell()
   
   time.sleep(1)
   print("[+] Successfully connected on target: " + target)
   print(f"[+] Command shell 1 sessions opened at: {current_time}" + "\n")
	
   while True:
    command = input("instasploit(" + Fore.RED + target + Style.RESET_ALL + ")> ")
   
    if command == "commands" or command == "help":
        play_command()
        print("\n=====================================================================")
        print("  COMMAND         DESCRIPTION                                        ")
        print("=====================================================================\n")
        print("- commands        List all commands                                  ")
        print("- sessions        List all sessions                                  ")
        print("- reconnect       Reconnectin to target                              ")
        print("- diconnect       Disconnecting target                               ")
        print("- execute         execute shell commands                             ")
        print("- manual          View program all information                       ")
        print("- leave           Log out by typing leave or exit                    ")
        print("- clear           Clear all screen                                   ")
        print("- check           Get connection check by destination                ")
        print("- addrss          Get all registered addressed by target photos      ")
        print("- captions        Get user's photos captions                         ")
        print("- comments        Get total comments of target's posts               ")
        print("- followers       Get target followers                               ")
        print("- followings      Get users followed by target                       ")
        print("- fwersemail      Get email of target followers                      ")
        print("- fwingsemail     Get email of users followed by target              ")
        print("- fwersnumber     Get phone number of target followers               ")
        print("- fwingsnumber    Get phone number of users followed by target       ")
        print("- hashtags        Get hashtags used by target                        ")
        print("- info            Get target info                                    ")
        print("- likes           Get total likes of target's posts                  ")
        print("- mediatype       Get user's posts type (photo or video)             ")
        print("- photodes        Get description of target's photos                 ")
        print("- photos          Download user's photos in output folder            ")
        print("- propic          Download user's profile picture                    ")
        print("- stories         Download user's stories                            ")
        print("- tagged          Get list of users tagged by target                 ")
        print("- wcommented      Get a list of user who commented target's photos   ")
        print("- wtagged         Get a list of user who tagged target               ")
        print("- tlikes          Get the likes of the entered person                ")
        print("- tcommnets       Get comments made by the entered person            ")
        print("- tfwilikes       Get posts that target followers like               ")
        print("- tfwicomment     Get comments the target makes on their followers   ")
        print("- ltfollowed      Get who followed the target last                   ")
        print("- ltiked          Get who liked the target's post last               ")
        print("- leave           Leave this program and exit\n                      ")
       
    elif command == "addrs":
        play_command()
        print("\n[*] Executing command: addrs...\n")
        profile = instaloader.Profile.from_username(L.context, target)
        posts = profile.get_posts()
        count = 0
        printed_header = False
    
        for post in posts:
            caption = post.caption
            location = post.location
            if location is not None:
                count += 1
                if not printed_header:  
                    print("================================================================== ")
                    print("                        TARGET LOCATION                            ")     
                    print("==================================================================\n")
                    printed_header = True  
                
                print(f"[+] location: {location.name} post number: {post.shortcode} ")
            else:
                if not printed_header:
                    print("================================================================== ")
                    print("                        TARGET LOCATION                            ")     
                    print("==================================================================\n")
                    printed_header = True
                    
                print(f"[-] No location information found for post number: {post.shortcode}" + "\n")
                
            if count == 12:
                break
     
    elif command == "captions":
        play_command() 
        print("\n[*] Executing command: captions...\n")
        profile = instaloader.Profile.from_username(L.context, target)
        posts = profile.get_posts()
        count = 0
        printed_header = False  

        for post in posts:
            caption = post.caption
            if caption is not None:
                count += 1
                if not printed_header:  
                    print("================================================================== ")
                    print("                         POST CAPTION                              ")     
                    print("==================================================================\n")
                    printed_header = True  
                
                print(f"[+] Post Number: {post.shortcode}\nCaption: {caption}\n")
            else:
                if not printed_header:
                    print("================================================================== ")
                    print("                         POST CAPTION                            ")     
                    print("==================================================================\n")
                    printed_header = True
                    
                print(f"[-] No caption found for post number: {post.shortcode}" + "\n")
                
            if count == 12:
                break  

    elif command == "comments": 
        play_command()
        print("\n[*] Executing command: comments...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            posts = profile.get_posts()
            count = 0
            printed_header = False  

            for post in posts:
                comments = post.get_comments()
                if comments:
                    count +=1
                    if not printed_header:
                        print("================================================================== ")
                        print("                         POST COMMENTS                              ")     
                        print("==================================================================\n")
                        printed_header = True  
                    print(f"[+] Post Number: {post.shortcode}\nComments: ")
                for comment in comments:
                    print(f"{comment.owner.username}: {comment.text}")
                print("\n")
            else:
                if not printed_header:
                    print("================================================================== ")
                    print("                         POST COMMENTS                            ")     
                    print("==================================================================\n")
                    printed_header = True

                print(f"[-] No comments found for post number: {post.shortcode}" + "\n")

            if count == 12:
                break 
        except:
            pass 

    elif command == "followers":
        play_command()
        print("\n[*] Executing command: followers...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followers = profile.get_followers()
            count = 0
            printed_header = False 

            for follower in followers:
                count += 1
                if not printed_header:  
                    print("================================================================== ")
                    print("                          FOLLOWERS                                 ")     
                    print("==================================================================\n")
                    printed_header = True

                print(f"[+] Follower: {follower.username}\n")

                if count == 12:
                    break
        except:
            pass

    elif command == "followings":
        play_command()
        print("\n[*] Executing command: followings...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followings = profile.get_followees()
            count = 0
            printed_header = False

            for following in followings:
                count += 1
                if not printed_header: 
                    print("================================================================== ")
                    print("                          FOLLOWINGS                                 ")     
                    print("==================================================================\n")
                    printed_header = True
                print(f"[+] Following: {following.username}\n")

            if count == 12:
                break
        except:
            pass

    elif command == "fwersemail":
        play_command()
        print("\n[*] Executing command: fwersemail...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followers = profile.get_followers()
            count = 0
            printed_header = False

            for follower in followers:
                email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', follower.biography)
                if email:
                    count += 1
                    if not printed_header:
                        print("================================================================== ")
                        print("                       FOLLOWER EMAIL ADDRESSES                     ")     
                        print("==================================================================\n")
                        printed_header = True
                    print(f"[+] Follower: {follower.username} - Email: {email[0]}\n")
                elif not printed_header and count == 0:
                    print("================================================================== ")
                    print("                       FOLLOWER EMAIL ADDRESSES                     ")     
                    print("==================================================================\n")
                    print("[*] Emails are being examined in detail...\n")
                    printed_header = True
                if count == 12 or count >= 100:
                    break
        except:
            pass

    elif command == "fwingsemail":
        play_command()
        print("\n[*] Executing command: fwingsemail...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followings = profile.get_followees()
            count = 0
            printed_header = False

            for following in followings:
                email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', following.biography)
                if email:
                    count += 1
                    if not printed_header:
                        print("================================================================== ")
                        print("                       FOLLOWING EMAIL ADDRESSES                    ")     
                        print("==================================================================\n")
                        printed_header = True
                    print(f"[+] Following: {following.username} - Email: {email[0]}\n")
                elif not printed_header and count == 0:
                    print("================================================================== ")
                    print("                       FOLLOWING EMAIL ADDRESSES                    ")     
                    print("==================================================================\n")
                    print("[*] Emails are being examined in detail...")
                    printed_header = True
                if count == 12 or count >= 100:
                    break
        except:
            pass

    elif command == "fwersnumber":
        play_command()
        print("\n[*] Executing command: fwersnumber...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followers = profile.get_followers()
            count = 0
            printed_header = False

            for follower in followers:
                phone_number = re.findall(r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', follower.biography)
                if phone_number:
                    count += 1
                    if not printed_header:
                        print("================================================================== ")
                        print("                      FOLLOWER PHONE NUMBERS                        ")     
                        print("==================================================================\n")
                        printed_header = True
                    print(f"[+] Follower: {follower.username} - Phone Number: {phone_number[0]}\n")
                elif not printed_header and count == 0:
                    print("================================================================== ")
                    print("                      FOLLOWER PHONE NUMBERS                        ")     
                    print("==================================================================\n")
                    print("[*] Numbers are being examined in detail\n")
                    printed_header = True
                if count == 12 or count >= 100:
                    break
        except:
            pass

    elif command == "fwingsnumber":
        play_command()
        print("\n[*] Executing command: fwingsnumber...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followings = profile.get_followees()
            count = 0
            printed_header = False

            for following in followings:
                phone_number = re.findall(r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', following.biography)
                if phone_number:
                    count += 1
                    if not printed_header:
                        print("================================================================== ")
                        print("                      FOLLOWING PHONE NUMBERS                        ")     
                        print("==================================================================\n")
                        printed_header = True
                    print(f"[+] Following: {following.username} - Phone Number: {phone_number[0]}\n")
                elif not printed_header and count == 0:
                    print("================================================================== ")
                    print("                      FOLLOWING PHONE NUMBERS                        ")     
                    print("==================================================================\n")
                    print("[*] Numbers are being examined in detail\n")
                    printed_header = True
                if count == 12 or count >= 100:
                    break
        except:
            pass

    elif command == "hashtags":
        play_command()
        print("\n[*] Executing command: hashtags...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            tagged_posts = profile.get_tagged_posts()
            hashtags = set()  

            for post in tagged_posts:
                for hashtag in post.caption_hashtags:
                    hashtags.add(hashtag)
    
            if len(hashtags) > 0:
                print("================================================================== ")
                print("                          TARGET HASHTAGS                           ")     
                print("==================================================================\n")
                for hashtag in hashtags:
                    print(f"[+] Hashtag: #{hashtag}\n")
            else:
                print("================================================================== ")
                print("                          TARGET HASHTAGS                           ")     
                print("==================================================================\n")
                print("[-] No hashtag found\n")
        except:
            pass

    elif command == "info":
        play_command()
        print("\n[*] Executing command: info...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)

            printed_header = False

            if not printed_header:
                print("================================================================== ")
                print("                          TARGET INFO                           ")     
                print("==================================================================\n")
                printed_header = True

            print(f"[+] Full Name: {profile.full_name}")
            print(f"[+] Username: {profile.username}")
            print(f"[+] Biography: {profile.biography}")
            print(f"[+] Website: {profile.external_url}")
            print(f"[+] Number of Posts: {profile.mediacount}")
            print(f"[+] Number of Followers: {profile.followers}")
            print(f"[+] Number of Followees: {profile.followees}" + "\n")
        except:
            pass

    elif command == "likes":
        play_command()
        print("\n[*] Executing command: likes...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            total_likes = 0
            post_count = 0
            printed_header = False

            for post in profile.get_posts():
                total_likes += post.likes
                post_count += 1

            if post_count > 0:
                avg_likes = total_likes / post_count
                print("================================================================== ")
                print("                          TARGET LIKES                           ")     
                print("==================================================================\n")
                print(f"[+] Total Likes: {total_likes}")
                print(f"[+] Number of Posts: {post_count}")
                print(f"[+] Average Likes per Post: {avg_likes:.2f}" + "\n")
                printed_header = True

            if not printed_header:
                print("================================================================== ")
                print("                          TARGET LIKES                           ")     
                print("==================================================================\n")
                print("[-] No posts found\n")
        except:
            pass

    elif command == "mediatype":
        play_command()
        print("\n[*] Executing command: mediatype...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            photos_count = 0
            videos_count = 0
            for post in profile.get_posts():
                if post.is_video:
                    videos_count += 1
            else:
                photos_count += 1
            print("================================================================== ")
            print("                       TARGET MEDIA TYPE                           ")
            print("==================================================================\n")
            print(f"[+] Target has {photos_count} photos and {videos_count} videos\n")
        except:
            pass

    elif command == "photodes":
        print("\n[*] Executing command: photodes...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            posts = profile.get_posts()
            printed_header = False

            for post in posts:
                if post.is_video:
                    continue
                if not printed_header:
                    print("================================================================== ")
                    print("                          PHOTO CAPTIONS                           ")     
                    print("==================================================================\n")
                    printed_header = True
                print(f"[+] Caption of photo {post.shortcode}: {post.caption}\n")
    
            if not printed_header:
                print("================================================================== ")
                print("                          PHOTO CAPTIONS                           ")     
                print("==================================================================\n")
                print("No photos found\n")
        except:
            pass

    elif command == "photos":

        play_command()
        print("\n[*] Executing command: photos...\n")
        
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            L.download_profile(profile, profile_pic=False)
            print("[+] Download completed successfully!\n")
            print("[+] Saved in: "+target)
        except:
            print("[!] Error download photos\n")
         
    elif command == "propic":
        play_command()
        print("\n[*] Executing command: propic...\n")
        try:
            rofile = instaloader.Profile.from_username(L.context, target)
            pic_url = profile.profile_pic_url
            filename = target + "_profile_pic.jpg"

            response = requests.get(pic_url)

            if response.status_code == 200:
                with open(filename, "wb") as file:
                    file.write(response.content)
                print("[+] Profile picture downloaded successfully!")
                print("[+] Saved as: " + filename +"\n")
            else:
                print("[-] Failed to download profile picture."+"\n")

        except:
            print("[!] Error download propic\n")

    elif command == "stories":
        play_command()
        print("\n[*] Executing command: stories...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            L.download_stories(userids=[profile.userid], filename_target='{date:%Y-%m-%d}')
            print("[+] Download completed successfully!")
            print("[+] Saved in: "+target+"\n")
        except:
            print("[!] Error download stories\n")

    elif command == "tagged":
        play_command()
        print("\n[*] Executing command: tagged...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            tagged_posts = profile.get_tagged_posts()
            printed_header = False
    
            for post in tagged_posts:
                if not printed_header:
                    print("================================================================== ")
                    print("                      TAGGED PHOTOS OF TARGET                     ")     
                    print("==================================================================\n")
                    printed_header = True
                print(f"[+] Tagged photo by {post.owner_username} in {post.shortcode}\n")
    
            if not printed_header:
                print("================================================================== ")
                print("                      TAGGED PHOTOS OF TARGET                     ")     
                print("==================================================================\n")
                print("[-] No tagged photos found\n")
        except:
            pass

    elif command == "wcommented":
        play_command()
        print("\n[*] Executing command: wcommented...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            commenters = {}

            for post in profile.get_posts():
                for comment in post.get_comments():
                    commenter = comment.owner
                    if commenter.username in commenters:
                        commenters[commenter.username] += 1
                    else:
                        commenters[commenter.username] = 1

            if len(commenters) > 0:
                sorted_commenters = sorted(commenters.items(), key=lambda x: x[1], reverse=True)
                print("================================================================== ")
                print("                        WHO COMMENTED MOST                         ")     
                print("==================================================================\n")
            for commenter, count in sorted_commenters:
                print(f"[+] {commenter} commented {count} times on target's posts\n")
            else:
                print("================================================================== ")
                print("                        WHO COMMENTED MOST                         ")     
                print("==================================================================\n")
                print("[-] No comments found on target's posts\n")
        except:
            pass

    elif command == "wtagged":
        play_command()
        print("\n[*] Executing command: wtagged...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            taggers = {}

            for post in profile.get_tagged_posts():
                for tag in post.caption_mentions: 
                    tagger = tag
                    if tagger in taggers:
                        taggers[tagger] += 1
                    else:
                        taggers[tagger] = 1

            if len(taggers) > 0:
                sorted_taggers = sorted(taggers.items(), key=lambda x: x[1], reverse=True)
                print("================================================================== ")
                print("                        WHO TAGGED THE TARGET                       ")
                print("==================================================================\n")
                for tagger, count in sorted_taggers:
                    print(f"[+] {tagger} tagged the target {count} times\n")
            else:
                print("================================================================== ")
                print("                        WHO TAGGED THE TARGET                       ")
                print("==================================================================\n")
                print("[-] No tags found on the target\n")
        except:
            pass

    elif command == "tlikes":
        play_command()
        print("\n[*] Executing command: tlikes...\n")
        try:
            target_user = input("[*] Enter target username: ")
            user = instaloader.Profile.from_username(L.context, target_user)
            user_posts = user.get_posts()

            likes = {}
            for post in user_posts:
                for like in post.get_likes():
                    if like.username == target:
                        if user.username in likes:
                            likes[user.username].append(post)
                        else:
                            likes[user.username] = [post]
                        
                time.sleep(5)
                    
            if len(likes) > 0:
                print("================================================================== ")
                print(f"            USERS WHO LIKED {target}'s POSTS                      ")     
                print("==================================================================\n")
                for user, posts in likes.items():
                    print(f"[+] {user} liked the following posts of {target}:")
                    for post in posts:
                        print(f"    - {post.url}" + "\n")
                    print("")
            else:
                print(f"[-] No posts liked by {target}" + "\n")
        except:
            pass

    elif command == "tcomments":
        play_command()
        print("\n[*] Executing command: tcomments...\n")
        try:
            target_user = input("[*] Enter the target username: ")
            user = instaloader.Profile.from_username(L.context, target_user)
            user_posts = user.get_posts()

            comments = {}
            for post in user_posts:
                for comment in post.get_comments():
                    if comment.owner.username == target:
                        if user.username in comments:
                            comments[user.username].append(comment)
                        else:
                            comments[user.username] = [comment]

                time.sleep(5)
                    
            if len(comments) > 0:
                print("================================================================== ")
                print(f"            USERS WHO COMMENTED ON {target}'s POSTS               ")     
                print("==================================================================\n")
                for user, comments in comments.items():
                    print(f"[+] {user} commented on the following posts of {target}:")
                    for comment in comments:
                        print(f"    - {comment.text}" + "\n")
                    print("")
            else:
                print(f"[-] No comments made by {target}" + "\n")
        except:
            pass

    elif command == "tfwilikes":
        play_command()
        print("\n[*] Executing command: tfiwilikes...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followees = set(profile.get_followees())
            liked_posts = {}

            for followee in followees:
                print(f"[+] Getting {followee.username}'s liked posts...")
                for post in followee.get_posts():
                    if post.likes > 0 and post.owner_username == target:
                        if followee.username in liked_posts:
                            liked_posts[followee.username].append(post)
                        else:
                            liked_posts[followee.username] = [post]

            if len(liked_posts) > 0:
                print("================================================================== ")
                print("            USERS WHO LIKED THE FOLLOWEES' POSTS OF TARGET         ")     
                print("==================================================================\n")
                for followee, posts in liked_posts.items():
                    print(f"[+] {followee} liked the following posts of the target:")
                    for post in posts:
                        print(f"    - {post.url}")
                    print("")
            else:
                print("================================================================== ")
                print("            USERS WHO LIKED THE FOLLOWEES' POSTS OF TARGET         ")     
                print("==================================================================\n")
                print("[-] No likes found on the followees' posts of the target\n")
        except:
            pass
        
    elif command == "tfwicomment":
        play_command()
        print("\n[*] Executing command: tfwicomment...\n")
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            followees = set(profile.get_followees())
            commented_posts = {}

            for followee in followees:
                print(f"[+] Getting {followee.username}'s commented posts...")
                for post in followee.get_posts():
                    comments = post.get_comments()
                    for comment in comments:
                        if comment.owner_username == target:
                            if followee.username in commented_posts:
                                commented_posts[followee.username].append((post.url, comment.text))
                            else:
                                commented_posts[followee.username] = [(post.url, comment.text)]

            if len(commented_posts) > 0:
                print("================================================================== ")
                print("          USERS WHO COMMENTED ON FOLLOWEES' POSTS OF TARGET       ")     
                print("==================================================================\n")
                for followee, posts_comments in commented_posts.items():
                    print(f"[+] {followee} commented on the following posts of the target:")
                    for post_comment in posts_comments:
                        print(f"    - Post URL: {post_comment[0]}")
                        print(f"      Comment: {post_comment[1]}")
                    print("")
            else:
                print("================================================================== ")
                print("          USERS WHO COMMENTED ON FOLLOWEES' POSTS OF TARGET       ")     
                print("==================================================================\n")
                print("[-] No comments found on the followees' posts of the target\n")
        except:
            pass

    elif command == "ltfollowed":
        play_command()
        print("\n[*] Executing command: ltfollowed...\n")
        print("================================================================== ")
        print("                        LAST FOLLOWED                             ")     
        print("==================================================================\n")
        
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            last_followed_user = None

            followers = profile.get_followers()
            for follower in followers:
                ast_followed_user = follower.username

            if last_followed_user:
                print("\n[+] Last followed user:", last_followed_user + "\n")
            else:
                print("\n[-] No followed user found.\n")
        except:
            pass
   
    elif command == "ltiked": 
        play_command()
        print("\n[*] Executing command: ltiked...\n")
        print("\n================================================================== ")
        print("                      LAST LIKED POST OWNER                         ")     
        print("==================================================================\n")      
        try:
            profile = instaloader.Profile.from_username(L.context, target)
            last_liked_post_owner = None
            last_liked_post_url = None

            posts = profile.get_posts()
            for post in posts:
                likes = list(post.get_likes())
                if likes:
                    last_liked_post_owner = likes[-1].username
                    last_liked_post_url = "https://www.instagram.com/p/" + post.shortcode
                    break

            if last_liked_post_owner:
                print("[+] Last liked post owner:", last_liked_post_owner)
                print("[+] Last liked post URL:", last_liked_post_url + "\n")
            else:
                print("\n[-] No liked post found.\n")
        except:
            pass
        
    elif command == "route":
        play_command()
        print("\n================================================================== ")
        print("                              ROUTE                               ")
        print("==================================================================\n")
        arrow_pos = 0 
        target_len = len(target) 

        while arrow_pos < target_len: 
            sys.stdout.write(f"\r[*] {username} {'=' * arrow_pos}> {' ' * (target_len - arrow_pos)} [*] {target}")
            sys.stdout.flush()
            arrow_pos += 1 
            time.sleep(0.5)
        print("\n[+] Routing complate\n") 
    
    elif command == "manual":
    	play_command()
    	print("\n[*] Getting information...")
    	time.sleep(1)
    	print("\n=====================================================================")
    	print("  INFO            DESCRIPTION                                        ")
    	print("=====================================================================\n")
    	print("- version:        v1.0                                               ")        
    	print("- Module:         Instaloader PyPI Instagram Api                     ")
    	print("- coder:          Anezatra Katedram                                  ")
    	print("- platform:       {}\n".format(platform.system()))                                  
    
    elif command == "sessions":
        play_command()
        print("\n=====================================================================")
        print("  TARGET                			INFORMATION                           ")
        print("=====================================================================\n")
        print(f"[*] {target}       Connection progress {current_time}          " + "\n")
    
    elif command == "reconnect":
        play_command()
        try:
            print("\n[*] Reconnecting https://instagram.com/" + target + "/...")
            profile = instaloader.Profile.from_username(L.context, target)
            print("[*] Command stager progress...")
            time.sleep(2)
            print("[+] Reconnected successfully: " + target +"\n")
        except:
            print("[-] Reconnected failure: failed to connect to target")
            print("[-] Please reboot the program or check your internet\n")

    elif command == "disconnect":
        play_command()
        print("\n[*] disconnecting to target...")
        time.sleep(1)
        print("[-] Command shell 1 sessions closed: user exit")
        print("[-] Connection closed\n") 
        os_shell()
    
    elif command == "execute":
        play_command()
        exec = input("\n[*] Execute: ")
        os.system(exec)
    
    elif command == "check":
        play_command()
        print("\n[*] Executing command: check...\n")
        time.sleep(1)
        print("[*] Checking connection stability...")
        profile = instaloader.Profile.from_username(L.context, target)
        if not profile.followed_by_viewer and profile.is_private:
            print("[-] Connection is not stable")
            print("[!] Please sending request\n")
        elif not profile.followed_by_viewer:
            print("\n[+] Connection stability")
            print("[-] You are not following this account\n")
        else:
            print("\n[+] Connection stability")
            print("[+] You are already following this account.\n")
    
    elif command == "clear":
            play_command()
            os.system("clear") 

    elif command == "leave" or command == "exit":
        sys.exit() 

def os_shell():
    while True:
        command = input("instasploit> ")
        if command == "commands" or command == "help":
            play_command()
            print("\n=====================================================================")
            print("  COMMAND         DESCRIPTION                                        ")
            print("=====================================================================\n")
            print("- commands        List all commands                                  ")
            print("- sessions        List all sessions                                  ")
            print("- cookies         Clear all cookies                                  ")
            print("- connect         Connecting to target                               ")
            print("- execute         Execute shell commands                             ")
            print("- manual          View program all information                       ")
            print("- leave           Log out by typing leave or exit                    ")
            print("- clear           Clear all screen                                 \n")
            
        elif command == "sessions":
            play_command()
            print("\n=====================================================================")
            print("  TARGET          INFORMATION                                        ")
            print("=====================================================================\n")
            print("[-] No connected from target                                            \n")
        
        elif command == "connect":
            play_command()
            shell()
        
        elif command == "manual":
            play_command()
            print("\n[*] Getting information...")
            time.sleep(1)
            print("\n=====================================================================")
            print("  INFO            DESCRIPTION                                        ")
            print("=====================================================================\n")
            print("- version:        v1.0                                               ")        
            print("- Module:         Instaloader PyPI Instagram Api                     ")
            print("- coder:          Anezatra Katedram                                  ")
            print("- platform:       {}\n".format(platform.system()))                              
           
            
        elif command == "leave":
            play_command()
            print("\n[-] Program shutdown\n")
            time.sleep(1)
            sys.exit()
        
        elif command == "execute":
            play_command()
            exec = input("\n[*] Execute: ")
            os.system(exec)
        
        elif command == "cookies":
            play_command()
            print("\n[*] Clearing Instaloader cookies...\n")
            os.system("rm -rf ~/.config/instaloader/*")
            print("[+] Cookies have been successfully cleared\n")

        elif command == "shell":
            play_command()
            main_shell()
        
        elif command == "reboot":
            play_command()
            print("\n[*] Rebooting...")
            time.sleep(2)
            main()
        
        elif command == "about":
            play_command()
            print("\n[*] Getting about...")
            time.sleep(1)
            print("\n=====================================================================")
            print("  INFO            DESCRIPTION                                        ")
            print("=====================================================================\n")
            print("- Coder:          Anezatra Katedram                                  ")
            print("- Contact:        Instagram: xx___xxbora_anezatraxx___x              ")
            print("- Email:          anezatra@gmail.com                                 ")
            print("- Note:           Please let me know if you find a bug in the program\n")

        elif command == "clear":
            play_command()
            if platform.system() == "Windows":
                os.system("cls")
            elif platform.system() == "Linux":
                os.system("clear")
			
def main():
 
  if platform.system() == "Windows":
    os.system("cls")
  elif platform.system() == "Linux":
    os.system("clear")
  play_start_sound()
  print("\n\n")
  print("       _____   ________________   _____ ____  __    ____  __________ ")
  print("      /  _/ | / / ___/_  __/   | / ___// __ \/ /   / __ \/  _/_  __/ ")
  print("      / //  |/ /\__ \ / / / /| | \__ \/ /_/ / /   / / / // /  / /    ")
  print("    _/ // /|  /___/ // / / ___ |___/ / ____/ /___/ /_/ // /  / /     ")
  print("   /___/_/ |_//____//_/ /_/  |_/____/_/   /_____/\____/___/ /_/      ")                                                               
  print("\n\n")
  print("                    * coded by Anezatra *                ")
  print("                  ===========================            ")
  print("                   INSTAGRAM DATA FRAMEWORK              ")
  print("                  ––·‹›·––·‹›·––·‹›·––·‹›·––·\n\n        ")
  print("WELCOME TO INSTASPLOIT V1.0")
  print("\nIt is illegal to use this program without the consent of the")
  print("target, without being directed towards the targets. The use   ")
  print("of the program is entirely the user's responsibility.         ")					   
  print("\n                    ** STARTING SUCCESSFULLY **             ")
  print("\n================================================================== ")
  print("                         INSTASPLOIT V1.0                            ")     
  print("================================================================== ")
  print("\n- Type 'commands' list all commands")
  print("- Type 'sessions' list all sessions")
  print("- Type 'connect' connecting to target")
  print("- Type 'manual' view program all information ")
  print("- Type 'reboot' program reboot and clear all data")
  print("- Type 'leave' Log out by typing leave or exit")  
  print("- Type 'about' view contact information\n") 
  os_shell()
                  	        
main()

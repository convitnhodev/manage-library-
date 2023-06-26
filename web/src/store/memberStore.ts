import memberService from '@/service/memberService';
import dayjs from 'dayjs';
import { observable, action } from 'mobx';

export interface IMember {
  id: number;
  name: string;
  type: string;
  dob: dayjs.Dayjs;
  address: string;
  email: string;
  created_at: dayjs.Dayjs;
}

class MemberStore {
  @observable memberData: IMember[] = [];

  @action getAll = async () => {
    try {
      const result = await memberService.getAll();
      this.memberData = result.data;
    } catch (error) {
      console.error('Error fetching members:', error);
    }
  };

  @action createNewMember = async (member: IMember) => {
    try {
      const result = await memberService.createNewMember(member);
      return result;
    } catch (error) {
      console.error('Error creating new member:', error);
    }
  };

  @action updateMember = async (member: IMember) => {
    try {
      const result = await memberService.updateMember(member);
      return result;
    } catch (error) {
      console.error('Error updating member:', error);
    }
  };

  @action deleteMember = async (id: number) => {
    try {
      const result = await memberService.deleteMember(id);
      return result;
    } catch (error) {
      console.error('Error deleting member:', error);
    }
  };
}

export default MemberStore;

// Legacy SaveOnBoardingState mutation removed - replaced with updateMyMetadata
// in useOnboardingStorage.ts for clean tenant-aware metadata updates
import { gql } from "@apollo/client";

export const WELCOME_PAGE_MUTATIONS_PLACEHOLDER = gql`
  fragment WelcomePageMutationsPlaceholder on Query {
    __typename
  }
`;
